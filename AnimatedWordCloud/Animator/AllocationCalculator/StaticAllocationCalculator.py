# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Calculate allocation of each words in each static time
"""

from typing import Literal, List
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from AnimatedWordCloud import WordVector, TimelapseWordVector
from AnimatedWordCloud.Animator import AllocationInFrame, AllocationTimelapse
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies import (
    allocate_magnetic,
)
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies import (
    Word,
)


def allocate(
    word_vector: WordVector,
    max_words: int,
    max_word_size: float,
    min_word_size: float,
    image_width: int,
    image_height: int,
    font_path: str,
    strategy: Literal["magnetic"] = "magnetic",
) -> AllocationInFrame:
    """
    Calculate allocation of each words in each static time

    :param WordVector word_vector: The word vector
    :param int max_words: Maximum number of words shown
    :param float max_word_size: Maximum size of the word
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :param str font_path: Path to the font
    :param str strategy: Strategy to allocate words.
    There are "magnetic" only for now.
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """

    word_weights = word_vector.get_ranking(0, max_words)

    words: List[Word] = []

    # get attributes for each words,
    #   and save them as Word instances
    for word_raw, weight in word_weights:
        # get attributes
        font_size = calculate_font_size(
            weight, word_weights[0][1], max_word_size, min_word_size
        )
        text_size = estimate_text_size(word_raw, font_size, font_path)

        # make instance
        word = Word(word_raw, weight, font_size, text_size)

        # save instance
        words.append(word)

    # calculate allocation by selected strategy
    if strategy == "magnetic":
        return allocate_magnetic(words, image_width, image_height)
    else:
        raise ValueError("Unknown strategy: {}".format(strategy))


def calculate_font_size(
    weight: float, weight_max: float, font_max: int, font_min: int
) -> int:
    """
    Evaluate how much font size the word should be

    Simply calculate linearly

    :param float weight: The weight of the word
    :param float weight_max: The maximum weight of the word
    :param int font_max: The maximum font size
    :param int font_min: The minimum font size
    :return: The font size estimated
    :rtype: int
    """

    # calculate font size linearly
    font_size = int((font_max - font_min) * (weight / weight_max) + font_min)

    return font_size


def estimate_text_size(word: str, font_size: int, font_path: str) -> (int, int):
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
    image = np.zeros((font_size * 2, font_size * (len(word) + 1), 3), dtype=np.uint8)
    font = ImageFont.truetype(font_path, font_size)
    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)

    # get size
    w, h = draw.textsize(word, font=font)

    return (w, h)


def allocate_all(timelapse: TimelapseWordVector) -> AllocationTimelapse:
    """
    Calculate allocation of each words in several each static time

    :param TimelapseWordVector timelapse: The word vector
    :return: Allocation data of each frame
    :rtype: AllocationTimelapse
    """

    times = len(timelapse)

    allocation_timelapse = AllocationTimelapse()

    # calculate allocation for each frame
    for cnt in range(times):
        allocation = allocate(timelapse[cnt].word_vector)
        allocation_timelapse.add(timelapse[cnt].time_name, allocation)

    return allocation_timelapse
