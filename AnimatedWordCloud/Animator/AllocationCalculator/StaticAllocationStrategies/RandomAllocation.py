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
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies import (
    StaticAllocationStrategy,
    Word,
    put_randomly,
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
            # put
            text_lefttop_position = put_randomly(
                self.image_width, self.image_height, word.text_size
            )

            # allocate in the output
            output[word.text] = (word.font_size, text_lefttop_position)

        return output
