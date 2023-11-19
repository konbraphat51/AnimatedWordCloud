# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Frontier of magnet at the center

Used by MagneticAllocation
"""


from __future__ import annotations
from collections.abc import Iterable
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies import (
    Rect,
    is_point_hitting_rects,
)


class MagnetOuterFrontier:
    """
    Outer frontier of the magnet at the center.
    This is used to find the next position of the next word.

    This described by launching a lazer from the boarder of the image;
        from up, down, left, and right.
    And find the first point that is not overlapped with the magnet.
    """

    def __init__(self) -> None:
        self.from_up: list[tuple[int, int]] = []
        self.from_down: list[tuple[int, int]] = []
        self.from_left: list[tuple[int, int]] = []
        self.from_right: list[tuple[int, int]] = []


def get_magnet_outer_frontier(
    rects_outermost: Iterable[Rect],
    image_width: int,
    image_height: int,
    image_division: int,
) -> tuple[MagnetOuterFrontier, set[Rect]]:
    """
    Find the outer frontier of the magnet at the center

    :param Iterable[Rect] rects_outermost: Rectangles that are currently putted at the outermost of the magnet
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :param int image_division: Number of division of the image
    :return: (Outer frontier of the magnet at the center,
        New list of rectangles that are currently putted at the outermost of the magnet)
    :rtype: tuple[MagnetOuterFrontier, set[Rect]]
    """

    X_INTERVAL = image_width / image_division
    Y_INTERVAL = image_height / image_division

    new_hitted_rects = set()

    magnet_outer_frontier = MagnetOuterFrontier()

    # from up
    for x in range(1, image_width, X_INTERVAL):
        for y in range(0, image_height + 1, Y_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects(
                (x, y), rects_outermost
            )
            if flag_hitted:
                new_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_up.append((x, y))
                break

    # from down
    for x in range(1, image_width, X_INTERVAL):
        for y in range(image_height, -1, -Y_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects(
                (x, y), rects_outermost
            )
            if flag_hitted:
                new_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_down.append((x, y))
                break

    # from left
    for y in range(1, image_height, Y_INTERVAL):
        for x in range(0, image_width + 1, X_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects(
                (x, y), rects_outermost
            )
            if flag_hitted:
                new_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_left.append((x, y))
                break

    # from right
    for y in range(1, image_height, Y_INTERVAL):
        for x in range(image_width, -1, -X_INTERVAL):
            flag_hitted, hitted_rect = is_point_hitting_rects(
                (x, y), rects_outermost
            )
            if flag_hitted:
                new_hitted_rects.add(hitted_rect)
                magnet_outer_frontier.from_right.append((x, y))
                break

    # update rects_outermost
    rects_outermost = new_hitted_rects

    return magnet_outer_frontier
