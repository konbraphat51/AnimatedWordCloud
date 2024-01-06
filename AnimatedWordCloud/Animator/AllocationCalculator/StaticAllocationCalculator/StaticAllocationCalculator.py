# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Calculate allocation of each words in each static time
"""

from __future__ import annotations
import numpy as np
from tqdm import tqdm
from PIL import Image, ImageFont, ImageDraw
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies import (
    MagneticAllocation,
    allocate_randomly,
)
from AnimatedWordCloud.Utils import (
    WordVector,
    TimelapseWordVector,
    AllocationInFrame,
    AllocationTimelapse,
    Word,
    Config,
)


def allocate(
    word_vector: WordVector,
    allocation_before: AllocationInFrame,
    config: Config,
) -> AllocationInFrame:
    """
    Calculate allocation of each words in each static time

    :param WordVector word_vector: The word vector
    :param AllocationInFrame allocation_before: Allocation data of the previous frame
    :param Config config: Config instance
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """

    word_weights = word_vector.get_ranking(0, config.max_words)

    words: list[Word] = []

    # get attributes for each words,
    #   and save them as Word instances
    for word_raw, weight in word_weights:
        # get size
        font_size = calculate_font_size(
            weight,
            word_weights[0][1],  # max weight
            word_weights[-1][1],  # min weight
            config.max_font_size,
            config.min_font_size,
        )
        text_size = estimate_text_size(word_raw, font_size, config.font_path)

        # make instance
        word = Word(word_raw, weight, font_size, text_size)

        # save instance
        words.append(word)

    # calculate allocation by selected strategy
    if config.allocation_strategy == "magnetic":
        allocator = MagneticAllocation(
            config.image_width,
            config.image_height,
            config.image_division,
            config.verbosity,
        )
        return allocator.allocate(words, allocation_before)
    else:
        raise ValueError(
            "Unknown strategy: {}".format(config.allocation_strategy)
        )


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
) -> tuple[int, int]:
    """
    Estimate text box size

    Highly depends on the drawing library

    :param str word: The word
    :param int font_size: The font size
    :param str font_path: The font path
    :return: Text box size (x, y)
    :rtype: tuple[int, int]
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
    w = draw.textlength(word, font=font, font_size=font_size)
    h = font_size

    return (w, h)


def allocate_all(
    timelapse: TimelapseWordVector, config: Config
) -> AllocationTimelapse:
    """
    Calculate allocation of each words in each static time

    :param TimelapseWordVector timelapse: The timelapse word vector
    :param Config config: Config instance
    :return: Allocation data of all the frames
    :rtype: AllocationTimelapse
    """

    times = len(timelapse)

    allocation_timelapse = AllocationTimelapse()

    # first frame
    first_frame = _allocate_first_frame(timelapse[0].word_vector, config)
    allocation_timelapse.add(config.starting_time_stamp, first_frame)

    # verbose for iteration
    if config.verbosity in ["debug", "minor"]:
        print("Start static-allocation iteration...")
        iterator = tqdm(range(times))
    else:
        iterator = range(times)

    # calculate allocation for each frame
    for cnt in iterator:
        allocation = allocate(
            timelapse[cnt].word_vector,
            allocation_timelapse.get_frame(
                cnt
            ),  # first added -> cnt; one before
            config,
        )
        allocation_timelapse.add(timelapse[cnt].time_name, allocation)

    return allocation_timelapse


def _allocate_first_frame(
    word_vector: WordVector, config: Config
) -> AllocationInFrame:
    """
    Calculate allocation of the first frame

    :param WordVector word_vector: The word vector
    :param Config config: Config instance
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """

    words_tup = word_vector.get_ranking(0, config.max_words)
    words = []  # Word instances

    # get attributes for each words,
    #   and save them as Word instances
    for word_raw, weight in words_tup:
        # minimum font size for the first frame
        text_size = estimate_text_size(
            word_raw, config.min_font_size, config.font_path
        )

        # make instance
        word = Word(word_raw, weight, config.min_font_size, text_size)

        # save instance
        words.append(word)

    # allocate randomly
    return allocate_randomly(words, config.image_width, config.image_height)
