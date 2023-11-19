# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Base class for static allocation strategies
"""

from collections.abc import Iterable
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    Word,
)
from AnimatedWordCloud.Animator import AllocationInFrame


class StaticAllocationStrategy:
    """
    Base class for static allocation strategies
    """

    def __init__(
        self,
        image_width: int,
        image_height: int,
        image_division: int = 100,
    ):
        self.image_width = image_width
        self.image_height = image_height
        self.image_division = image_division

    def allocate(
        self, words: Iterable[Word], allocation_before: AllocationInFrame
    ) -> AllocationInFrame:
        """
        Allocate the words

        This is abstract method.

        :param Iterable[Word] words: The words to allocate
        :param AllocationInFrame allocation_before: The allocation data of the previous frame
        """

        raise NotImplementedError
