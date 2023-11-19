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
from collections.abc import Iterable
from random import random
from math import sin, cos, pi
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies import (
    StaticAllocationStrategy,
    Word,
)
from AnimatedWordCloud.Animator import AllocationInFrame


class RandomAllocation(StaticAllocationStrategy):
    """
    First static allocation strategy.

    Randomly allocate words AROUND the image.

    This is used for the very first frame, before the first timelapse.
    """

    def allocate(self, words: Iterable[Word]) -> AllocationInFrame:
        """
        Allocate the words

        :param Iterable[Word] words: The words to allocate
        :return: Allocation data of the frame
        :rtype: AllocationInFrame
        """

        output = AllocationInFrame()

        for word in words:
            # calculate the radius of the circle
            image_diagnal = (
                self.image_width**2 + self.image_height**2
            ) ** 0.5
            text_diagnal = (
                word.text_size[0] ** 2 + word.text_size[1] ** 2
            ) ** 0.5
            radius = (image_diagnal + text_diagnal) / 2

            # randomly choose where on the circle to put
            angle = random() * 2 * pi
            image_center_x = self.image_width / 2
            image_center_y = self.image_height / 2
            x = image_center_x + radius * cos(angle)
            y = image_center_y + radius * sin(angle)
            text_lefttop_position = (
                x - word.text_size[0] / 2,
                y - word.text_size[1] / 2,
            )

            # allocate in the output
            output[word.text] = (word.font_size, text_lefttop_position)

        return output