# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
One strategy to allocate words in static time.

First, put the largest word in the center.
Regard this word as a magnet.
Then, put the next largest word at empty point, 
    contacting with the magnet at the center.
The point will be evaluated by evaluate_position(),
    and the most best point will be selected.
Repeating this process, all words will be allocated.
"""

from typing import Tuple
from collections.abc import Iterable
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    Word,
)
from AnimatedWordCloud.Animator import AllocationInFrame

class Rect:
    def __init__(self, left_top: Tuple[int, int], right_bottom: Tuple[int, int]):
        self.left_top = left_top
        self.right_bottom = right_bottom

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
    
    # Word rectangles that already putted
    rects_putted = []
    
    #put the first word at the center
    center = (image_width / 2, image_height / 2)
    first_word = words[0]
    first_word_position = (center[0] - first_word.text_size[0] / 2, center[1] - first_word.text_size[1] / 2)
   
    #register
    rects_putted.append(Rect(first_word_position, (first_word_position[0] + first_word.text_size[0], first_word_position[1] + first_word.text_size[1])))

def evaluate_position(
    position_from: Tuple[int, int],
    position_to: Tuple[int, int],
    center: Tuple[int, int],
) -> float:
    return 1.0  # temp
