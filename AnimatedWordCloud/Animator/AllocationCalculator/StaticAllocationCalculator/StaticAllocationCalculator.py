# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Calculate allocation of each words in each static time
"""

from typing import Literal
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from AnimatedWordCloud.Animator.TimelapseWordVector import WordVector, TimelapseWordVector
from AnimatedWordCloud.Animator.AllocationData import AllocationInFrame, AllocationTimelapse
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies import (
    MagneticAllocation,
    Word,
    allocate_randomly,
)
from AnimatedWordCloud.Utils import TRANSITION_SYMBOL


def allocate(
    word_vector: WordVector,
    allocation_before: AllocationInFrame,
    max_words: int,
    max_font_size: float,
    min_font_size: float,
    image_width: int,
    image_height: int,
    font_path: str,
    strategy: Literal["magnetic"] = "magnetic",
    image_division: int = 100,
) -> AllocationInFrame:
    """
    Calculate allocation of each words in each static time

    :param WordVector word_vector: The word vector
    :param AllocationInFrame allocation_before: Allocation data of the previous frame
    :param int max_words: Maximum number of words shown
    :param float max_font_size: Maximum font size of the word
    :param float min_font_size: Minimum font size of the word
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :param str font_path: Path to the font
    :param str strategy: Strategy to allocate words.
        There are "magnetic" only for now.
    :param int image_division: The number of division of the image.
        Used by magnetic strategy.
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """

    word_weights = word_vector.get_ranking(0, max_words)

    words: list[Word] = []

    # get attributes for each words,
    #   and save them as Word instances
    for word_raw, weight in word_weights:
        # get attributes
        font_size = calculate_font_size(
            weight,
            word_weights[0][1],
            word_weights[-1][1],
            max_font_size,
            min_font_size,
        )
        text_size = estimate_text_size(word_raw, font_size, font_path)

        # make instance
        word = Word(word_raw, weight, font_size, text_size)

        # save instance
        words.append(word)

    # calculate allocation by selected strategy
    if strategy == "magnetic":
        allocator = MagneticAllocation(
            image_width, image_height, image_division
        )
        return allocator.allocate(words, allocation_before)
    else:
        raise ValueError("Unknown strategy: {}".format(strategy))


def calculate_font_size(
    weight: float,
    weight_max: float,
    weight_min: float,
    font_max: int,
    font_min: int,
) -> int:
    """
    Evaluate how much font size the word should be

    Simply calculate linearly

    :param float weight: The weight of the word
    :param float weight_max: The maximum weight of the word
    :param float weight_min: The minimum weight of the word
    :param int font_max: The maximum font size
    :param int font_min: The minimum font size
    :return: The font size estimated
    :rtype: int
    """

    # calculate font size linearly
    weight_ratio = (weight - weight_min) / (weight_max - weight_min)
    font_size = int((font_max - font_min) * weight_ratio + font_min)

    return font_size


def estimate_text_size(
    word: str, font_size: int, font_path: str
) -> (int, int):
    """
    Estimate text box size

    Highly depends on the drawing library

    :param str word: The word
    :param int font_size: The font size
    :param str font_path: The font path
    :return: Text box size (x, y)
    :rtype: (int, int)
    """

    # according to https://watlab-blog.com/2019/08/27/add-text-pixel/

    # prepare empty image
    image = np.zeros(
        (font_size * 2, font_size * (len(word) + 1), 3), dtype=np.uint8
    )
    font = ImageFont.truetype(font_path, font_size)
    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)

    # get size
    w, h = draw.textsize(word, font=font)

    return (w, h)


def allocate_all(
    timelapse: TimelapseWordVector,
    max_words: int,
    max_font_size: float,
    min_font_size: float,
    image_width: int,
    image_height: int,
    font_path: str,
    strategy: Literal["magnetic"] = "magnetic",
    image_division: int = 100,
) -> AllocationInFrame:
    """
    Calculate allocation of each words in each static time

    :param TimelapseWordVector timelapse: The timelapse word vector
    :param int max_words: Maximum number of words shown
    :param float max_font_size: Maximum font size of the word
    :param float min_font_size: Minimum font size of the word
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :param str font_path: Path to the font
    :param str strategy: Strategy to allocate words.
        There are "magnetic" only for now.
    :param int image_division: The number of division of the image.
        Used by magnetic strategy.
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """

    times = len(timelapse)

    allocation_timelapse = AllocationTimelapse()

    # first frame
    first_frame = allocate_randomly(
        timelapse[0].word_vector, image_width, image_height
    )
    allocation_timelapse.add(
        TRANSITION_SYMBOL + timelapse[0].time_name, first_frame
    )

    # calculate allocation for each frame
    for cnt in range(times):
        allocation = allocate(
            timelapse[cnt].word_vector,
            allocation_timelapse.get_frame(cnt - 1),
            max_words,
            max_font_size,
            min_font_size,
            image_width,
            image_height,
            font_path,
            strategy,
            image_division,
        )
        allocation_timelapse.add(timelapse[cnt].time_name, allocation)

    return allocation_timelapse
