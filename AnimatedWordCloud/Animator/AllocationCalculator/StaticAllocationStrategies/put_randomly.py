# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Function to put a word randomly on the image.

This is the method for RandomAllocation.py, 
    but it is also used in other allocation strategies.
So, this is seperated from RandomAllocation.py 
    for avoiding circular reference.
"""

from random import random
from math import sin, cos, pi


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
