# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
First static allocation strategy.

Randomly allocate words AROUND the image.
Words are put on randomly 
    on a circle, whose center is the center of the image,
    and whose radius is 
    (the diagonal length of the image + the diagonal length of the word)/2
    which don't let the word overlap with the image in this frame.

This is used for the very first frame, before the first timelapse.
"""

from __future__ import annotations
from typing import Iterable
from random import random
from math import pi, cos, sin
from AnimatedWordCloud.Utils import Word, AllocationInFrame


def allocate_randomly(
    words: Iterable[Word], image_width: int, image_height: int
) -> AllocationInFrame:
    """
    Allocate the words

    :param Iterable[Word] words: The words to allocate
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """

    output = AllocationInFrame(from_static_allocation=True)

    for word in words:
        # put
        text_lefttop_position = put_randomly(
            image_width, image_height, word.text_size
        )

        # allocate in the output
        output.add(word.text, word.font_size, text_lefttop_position)

    return output


def put_randomly(
    image_width: int, image_height: int, word_size: tuple[int, int]
) -> tuple[int, int]:
    """
    Randomly allocate word AROUND the image.

    Words are put on randomly
        on a circle, whose center is the center of the image,
        and whose radius is
        (the diagonal length of the image + the diagonal length of the word)/2
        which don't let the word overlap with the image in this frame.

    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :param tuple[int, int] word_size: Size of the word
    :return: Left-top position of the word
    :rtype: tuple[int, int]
    """
    # calculate the radius of the circle
    image_diagnal = (image_width**2 + image_height**2) ** 0.5
    text_diagnal = (word_size[0] ** 2 + word_size[1] ** 2) ** 0.5
    radius = (image_diagnal + text_diagnal) / 2

    # randomly choose where on the circle to put
    angle = random() * 2 * pi
    image_center_x = image_width / 2
    image_center_y = image_height / 2
    x = image_center_x + radius * cos(angle)
    y = image_center_y + radius * sin(angle)
    text_lefttop_position = (
        x - word_size[0] / 2,
        y - word_size[1] / 2,
    )

    return text_lefttop_position
