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
    is_point_hitting_rect,
)
from AnimatedWordCloud.Utils import Vector


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

    # prepare for iteration
    launcher_start_positions = [
        Vector(0, 0),  # from up
        Vector(0, image_height),  # from down
        Vector(0, 0),  # from left
        Vector(image_width, 0),  # from right
    ]
    launcher_directions = [
        Vector(X_INTERVAL, 0),  # from up
        Vector(X_INTERVAL, 0),  # from down
        Vector(0, Y_INTERVAL),  # from left
        Vector(0, Y_INTERVAL),  # from right
    ]
    detection_ray_directions = [
        Vector(0, Y_INTERVAL),  # from up
        Vector(0, -Y_INTERVAL),  # from down
        Vector(X_INTERVAL, 0),  # from left
        Vector(-X_INTERVAL, 0),  # from right
    ]
    corresponding_frontiers = []

    # detect from 4 sides
    for cnt in range(4):
        # detect
        detected_points, new_hitted_rects_here = _detect_frontier_linealy(
            launcher_start_positions[cnt],
            launcher_directions[cnt],
            detection_ray_directions[cnt],
            rects_outermost,
            image_width,
            image_height,
        )

        # update
        corresponding_frontiers.append(detected_points)
        new_hitted_rects |= new_hitted_rects_here

    # update magnet_outer_frontier
    magnet_outer_frontier.from_up = corresponding_frontiers[0]
    magnet_outer_frontier.from_down = corresponding_frontiers[1]
    magnet_outer_frontier.from_left = corresponding_frontiers[2]
    magnet_outer_frontier.from_right = corresponding_frontiers[3]

    return (magnet_outer_frontier, new_hitted_rects)


def _detect_frontier_linealy(
    launcher_point_start: Vector,
    launcher_direction: Vector,
    detection_ray_direction: Vector,
    rects_outermost: Iterable[Rect],
    image_width: int,
    image_height: int,
) -> tuple[list[tuple[int, int]], set[Rect]]:
    """
    Detect the frontier from 1 line.

    This first set a launcher at the starting point.
    Then launch a detection ray from the launcher,
        and move the detection ray until some rect hits.
    Then move the launcher and the detection ray in the same direction,
        again and again, until the launcher is out of the image.

    :param Vector launcher_point_start:
        Starting point of the detection ray launching position
    :param Vector launcher_points_direction:
        Direction vector of the launching position moves
    :param Vector detection_ray_direction:
        Direction vector of the detection ray moves
    :param Iterable[Rect] rects_outermost:
        Rectangles that are currently putted at the outermost of the magnet
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :return: (List of points that are detected,
        New list of rectangles that are
        currently putted at the outermost of the magnet)
    :rtype: tuple[list[tuple[int, int]], set[Rect]]
    """

    detected_points = []
    rects_outermost = set()

    image_size = (image_width, image_height)

    launcher_position = launcher_point_start.clone()
    # whicle lancher is inside the image...
    while is_point_hitting_rect(image_size, launcher_position):
        # launch the ray
        detection_ray_position = launcher_position.clone()

        # while detection ray is inside the image...
        while is_point_hitting_rect(image_size, detection_ray_position):
            # check hit
            flag_hitted, hitted_rect = is_point_hitting_rects(
                detection_ray_position, rects_outermost
            )

            if flag_hitted:
                # register
                rects_outermost.add(hitted_rect)
                detected_points.append(
                    detection_ray_position.convert_to_tuple()
                )
                break

            # move detection ray
            detection_ray_position += detection_ray_direction

        # move launcher
        launcher_position += launcher_direction

    return detected_points, rects_outermost
