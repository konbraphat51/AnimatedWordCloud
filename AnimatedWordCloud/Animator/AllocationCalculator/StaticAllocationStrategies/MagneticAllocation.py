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

from typing import Tuple, Set
from collections.abc import Iterable
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    Word,
)
from AnimatedWordCloud.Animator import AllocationInFrame
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies import (
    Rect,
    is_point_hitting_rects,
)
import math


class MagnetOuterFrontier:
    """
    Outer frontier of the magnet at the center.
    This is used to find the next position of the next word.

    This described by launching a lazer from the boarder of the image;
        from up, down, left, and right.
    And find the first point that is not overlapped with the magnet.
    """

    def __init__(self) -> None:
        self.from_up: Tuple[int, int] = []
        self.from_down: Tuple[int, int] = []
        self.from_left: Tuple[int, int] = []
        self.from_right: Tuple[int, int] = []


def allocate_magnetic(
    words: Iterable[Word],
    allocation_before: AllocationInFrame,
    image_width: int,
    image_height: int,
    image_division: int = 100,
) -> AllocationInFrame:
    """
    Allocate words in magnetic strategy

    :param Iterable[Word] words: Words to allocate. Order changes the result.
    :param AllocationInFrame allocation_before: Allocation data at one static frame before
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :param int image_division: How much the image is divided when finding a new position.
    The more means the more precise but the more time-consuming.
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """

    output = AllocationInFrame()

    # Word rectangles that are currenly putted
    #   at the oytermost of the magnet
    rects_outermost = set()

    # put the first word at the center
    center = (image_width / 2, image_height / 2)
    first_word = words[0]
    first_word_position = (
        center[0] - first_word.text_size[0] / 2,
        center[1] - first_word.text_size[1] / 2,
    )

    # register
    rects_outermost.add(
        Rect(
            first_word_position,
            (
                first_word_position[0] + first_word.text_size[0],
                first_word_position[1] + first_word.text_size[1],
            ),
        )
    )
    output.add(first_word.text, first_word.font_size, first_word_position)

    # avoid index exceeded error
    if len(words) == 1:
        return output

    # from second word
    for word in words[1:]:
        magnet_outer_frontier, rects_outermost = find_magnet_outer_frontier(
            rects_outermost, image_width, image_height, image_division
        )


def evaluate_position(
    position_from: Tuple[int, int],
    position_to: Tuple[int, int],
    center: Tuple[int, int],
) -> float:
    """
    Evaluate the position the word beginf to put

    :param Tuple[int,int] position_from: Position of the center of the word comming from
    :param Tuple[int,int] position_to: Position of the center of the word going to be putted
    :param Tuple[int,int] center: Position of the center of the magnet
    :return: Evaluation value. Smaller is the better
    """

    distance_movement = math.sqrt(
        (position_from[0] - position_to[0]) ** 2
        + (position_from[1] - position_to[1]) ** 2
    )

    distance_center = math.sqrt(
        (position_to[0] - center[0]) ** 2 + (position_to[1] - center[1]) ** 2
    )

    # the smaller, the better; This need manual adjustment
    return distance_movement**2 + distance_center**2


def find_magnet_outer_frontier(
    rects_outermost: Iterable[Rect],
    image_width: int,
    image_height: int,
    image_division: int,
) -> Tuple[MagnetOuterFrontier, Set[Rect]]:
    """
    Find the outer frontier of the magnet at the center

    :param Iterable[Rect] rects_outermost: Word rectangles that are currenly putted
        at the oytermost of the magnet
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :param int image_division: How much the image is divided when finding a new position.
    :return: (Outer frontier of the magnet at the center,
                updated outermost rects)
    :rtype: Tuple[MagnetOuterFrontier, Set[Rect]]
    """

    X_INTERVAL = image_width / image_division
    Y_INTERVAL = image_height / image_division

    current_hitted_rects = set()

    magnet_outer_frontier = MagnetOuterFrontier()

    # from up
    for x in range(1, image_width, X_INTERVAL):
        for y in range(0, image_height + 1, Y_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects(
                (x, y), rects_outermost
            )
            if flag_hitted:
                current_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_up.append((x, y))
                break

    # from down
    for x in range(1, image_width, X_INTERVAL):
        for y in range(image_height, -1, -Y_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects(
                (x, y), rects_outermost
            )
            if flag_hitted:
                current_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_down.append((x, y))
                break

    # from left
    for y in range(1, image_height, Y_INTERVAL):
        for x in range(0, image_width + 1, X_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects(
                (x, y), rects_outermost
            )
            if flag_hitted:
                current_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_left.append((x, y))
                break

    # from right
    for y in range(1, image_height, Y_INTERVAL):
        for x in range(image_width, -1, -X_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects(
                (x, y), rects_outermost
            )
            if flag_hitted:
                current_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_right.append((x, y))
                break

    return (magnet_outer_frontier, current_hitted_rects)
