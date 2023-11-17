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


class Rect:
    def __init__(self, left_top: Tuple[int, int], right_bottom: Tuple[int, int]):
        self.left_top = left_top
        self.right_bottom = right_bottom


class MagnetOuterFrontier:
    """
    Outer frontier of the magnet at the center.
    This is used to find the next position of the next word.

    This described by launching a lazer from the boarder of the image;
        from up, down, left, and right.
    And find the first point that is not overlapped with the magnet.
    """

    def __init__(
        self,
        from_up: Tuple[int, int],
        from_down: Tuple[int, int],
        from_left: Tuple[int, int],
        from_right: Tuple[int, int],
    ):
        self.from_up: Tuple[int, int] = []
        self.from_down: Tuple[int, int] = []
        self.from_left: Tuple[int, int] = []
        self.from_right: Tuple[int, int] = []


def allocate_magnetic(
    words: Iterable[Word],
    image_width: int,
    image_height: int,
    image_division: int = 100,
) -> AllocationInFrame:
    """
    Allocate words in magnetic strategy

    :param Iterable[Word] words: Words to allocate. Order changes the result.
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
        pass


def evaluate_position(
    position_from: Tuple[int, int],
    position_to: Tuple[int, int],
    center: Tuple[int, int],
) -> float:
    return 1.0  # temp


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
            flag_hitted, hitted_rect = is_point_hitting_rects((x, y), rects_outermost)
            if flag_hitted:
                current_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_up.append((x, y))
                break

    # from down
    for x in range(1, image_width, X_INTERVAL):
        for y in range(image_height, -1, -Y_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects((x, y), rects_outermost)
            if flag_hitted:
                current_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_down.append((x, y))
                break

    # from left
    for y in range(1, image_height, Y_INTERVAL):
        for x in range(0, image_width + 1, X_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects((x, y), rects_outermost)
            if flag_hitted:
                current_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_left.append((x, y))
                break

    # from right
    for y in range(1, image_height, Y_INTERVAL):
        for x in range(image_width, -1, -X_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects((x, y), rects_outermost)
            if flag_hitted:
                current_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_right.append((x, y))
                break

    return (magnet_outer_frontier, current_hitted_rects)


def is_point_hitting_rects(
    self, point: Tuple[int, int], rects: Iterable[Rect]
) -> Tuple[bool, Rect]:
    """
    Check if the point is hitting any of the rects given.

    :param Tuple[int,int] point: Point to check
    :param Iterable[Rect] rects: Rectangles to check
    :return: (Is hitting, Rect that is hitting)
    :rtype: Tuple[bool, Rect]
    """
    for rect in rects:
        if is_point_hitting_rect(point, rect):
            return (True, rect)

    return (False, None)


def is_point_hitting_rect(self, point: Tuple[int, int], rect: Rect) -> bool:
    """
    Check if the point is hitting the single rect given.

    :param Tuple[int,int] point: Point to check
    :param Rect rect: Rectangle to check
    :return: Is hitting
    :rtype: bool
    """
    return (
        rect.left_top[0] <= point[0] <= rect.right_bottom[0]
        and rect.left_top[1] <= point[1] <= rect.right_bottom[1]
    )
