# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Collision detection functions
"""

from __future__ import annotations
from typing import Iterable
from AnimatedWordCloud.Utils.Vector import Vector
from AnimatedWordCloud.Utils.Data.Rect import Rect


def is_point_hitting_rects(
    point: tuple[int, int] | Vector, rects: Iterable[Rect]
) -> tuple[bool, Rect]:
    """
    Check if the point is hitting any of the rects given.

    :param Tuple[int,int]|Vector point: Point to check
    :param Iterable[Rect] rects: Rectangles to check
    :return: (Is hitting, Rect that is hitting)
    :rtype: Tuple[bool, Rect]
    """
    for rect in rects:
        if is_point_hitting_rect(point, rect):
            return (True, rect)

    return (False, None)


def is_point_hitting_rect(point: tuple[int, int] | Vector, rect: Rect) -> bool:
    """
    Check if the point is hitting the single rect given.

    :param Tuple[int,int]|Vector point: Point to check
    :param Rect rect: Rectangle to check
    :return: Is hitting
    :rtype: bool
    """

    if point.__class__ == tuple:
        point = Vector(point)

    return (
        rect.left_top[0] < point.x < rect.right_bottom[0]
        and rect.left_top[1] < point.y < rect.right_bottom[1]
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
