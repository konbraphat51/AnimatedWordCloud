# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
One strategy to allocate words in static time.

First, put the largest word in the center.
Then, put the next largest word at empty point.
The point will be evaluated by evaluate_position().
Repeating this process, all words will be allocated.
"""

from typing import Tuple
from collections.abc import Iterable
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    Word,
)
from AnimatedWordCloud.Animator import AllocationInFrame


def allocate_magnetic(
    words: Iterable[Word], image_width: int, image_height: int
) -> AllocationInFrame:
    """
    Allocate words in magnetic strategy

    :param Iterable[Word] words: Words to allocate. Order changes the result.
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """
    pass


def evaluate_position(
    position_from: Tuple[int, int],
    position_to: Tuple[int, int],
    center: Tuple[int, int],
) -> float:
    return 1.0  # temp
