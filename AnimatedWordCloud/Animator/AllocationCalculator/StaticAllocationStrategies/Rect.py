# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Handling rect in static allocation strategies
"""

from __future__ import annotations
from collections.abc import Iterable


class Rect:
    def __init__(
        self, left_top: tuple[int, int], right_bottom: tuple[int, int]
    ) -> None:
        """
        :param Tuple[int,int] left_top: Left top position of the rect
        :param Tuple[int,int] right_bottom: Right bottom position of the rect
        """
        self.left_top = left_top
        self.right_bottom = right_bottom


def is_point_hitting_rects(
    point: tuple[int, int], rects: Iterable[Rect]
) -> tuple[bool, Rect]:
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


def is_point_hitting_rect(point: tuple[int, int], rect: Rect) -> bool:
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


def is_rect_hitting_rect(rect0: Rect, rect1: Rect) -> bool:
    """
    Check if 2 rects hitting

    Check the collision by AABB algorithm

    :param Rect rect0: Rect to check
    :param Rect rect1: Rect to check
    :return: Whether 2 rects are hitting
    :rtype: bool
    """

    return not (
        rect0.right_bottom[0] < rect1.left_top[0]
        or rect0.left_top[0] > rect1.right_bottom[0]
        or rect0.right_bottom[1] < rect1.left_top[1]
        or rect0.left_top[1] > rect1.right_bottom[1]
    )


def is_rect_hitting_rects(rect: Rect, rects: Iterable[Rect]) -> bool:
    """
    Check if the rect is hitting any of the rects given.

    :param Rect rect: Rect to check
    :param Iterable[Rect] rects: Rectangles to check
    :return: Is hitting
    :rtype: bool
    """
    for rect_to_check in rects:
        if is_rect_hitting_rect(rect, rect_to_check):
            return True

    return False
