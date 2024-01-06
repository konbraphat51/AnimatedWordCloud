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
from typing import Iterable
from bisect import bisect
from AnimatedWordCloud.Utils import (
    Vector,
    Rect,
    is_point_hitting_rects,
    is_point_hitting_rect,
)

TO_RIGHT = Vector(0, 0)
TO_LEFT = Vector(0, 0)
TO_UP = Vector(0, 0)
TO_DOWN = Vector(0, 0)


class MagnetOuterFrontier:
    """
    Outer frontier of the magnet at the center.
    This is used to find the next position of the next word.

    This described by launching a lazer from the boarder of the image;
        from up, down, left, and right.
    And find the first point that is not overlapped with the magnet.
    """

    def __init__(self) -> None:
        """
        Make empty data
        """

        self.from_up: list[tuple[int, int]] = []
        self.from_down: list[tuple[int, int]] = []
        self.from_left: list[tuple[int, int]] = []
        self.from_right: list[tuple[int, int]] = []


def get_magnet_outer_frontier(
    rects: Iterable[Rect],
    image_width: int,
    image_height: int,
    interval_x: float,
    interval_y: float,
    rect_added: Rect,
    frontier_former: MagnetOuterFrontier,
) -> MagnetOuterFrontier:
    """
    Find the outer frontier of the magnet at the center

    :param Iterable[Rect] rects: Rectangles that are currently putted in the magnet
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :param int interval_x: interval of the precision; x
    :param int interval_y: interval of the precision; y
    :param Rect rect_added: Rectangle that is added at the last step. If specified with frontier_former, the calculation is faster.
    :param MagnetOuterFrontier frontier_former: Former frontier. If specified with rect_added, the calculation is faster.
    :return: Outer frontier of the magnet at the center
    :rtype: MagnetOuterFrontier
    """

    _initialize_directions(interval_x, interval_y)

    magnet_outer_frontier = MagnetOuterFrontier()

    # prepare for iteration
    # need to shift 1 for the collision detection
    launcher_start_positions = [
        Vector(1, 1),  # from up
        Vector(1, image_height - 1),  # from down
        Vector(1, 1),  # from left
        Vector(image_width - 1, 1),  # from right
    ]
    launcher_directions = [
        TO_RIGHT,  # from up
        TO_RIGHT,  # from down
        TO_DOWN,  # from left
        TO_DOWN,  # from right
    ]
    detection_ray_directions = [
        TO_DOWN,  # from up
        TO_UP,  # from down
        TO_RIGHT,  # from left
        TO_LEFT,  # from right
    ]
    former_frontiers_by_side = [
        frontier_former.from_up,  # from up
        frontier_former.from_down,  # from down
        frontier_former.from_left,  # from left
        frontier_former.from_right,  # from right
    ]

    # detect from 4 sides
    corresponding_frontiers = []
    for cnt in range(4):
        # detect
        detected_points = _detect_frontier_linealy(
            launcher_start_positions[cnt],
            launcher_directions[cnt],
            detection_ray_directions[cnt],
            rects,
            image_width,
            image_height,
            rect_added,
            former_frontiers_by_side[cnt],
        )

        # update
        corresponding_frontiers.append(detected_points)

    # update magnet_outer_frontier
    magnet_outer_frontier.from_up = corresponding_frontiers[0]
    magnet_outer_frontier.from_down = corresponding_frontiers[1]
    magnet_outer_frontier.from_left = corresponding_frontiers[2]
    magnet_outer_frontier.from_right = corresponding_frontiers[3]

    return magnet_outer_frontier


def _detect_frontier_linealy(
    launcher_point_start: Vector,
    launcher_direction: Vector,
    detection_ray_direction: Vector,
    rects: Iterable[Rect],
    image_width: int,
    image_height: int,
    rect_added: Rect,
    frontier_former_side: list[tuple[int, int]],
) -> list[tuple[int, int]]:
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
    :param Iterable[Rect] rects:
        Word's Rectangles that are currently putted in the magnet
    :param int image_width: Width of the image
    :param int image_height: Height of the image
    :param Rect rect_added: Rectangle that is added at the last step.
    :param list[tuple[int, int]] frontier_former_side: List of points of a side if former frontier.
    :return: List of points that are detected
    :rtype: list[tuple[int, int]]
    """
    # a clone made
    frontier_former_side = _sort_by_direction(
        frontier_former_side, detection_ray_direction
    )

    # true while the launcher is in the area hitting the rect_added
    hitting = False

    detected_points = []
    image_size = (image_width, image_height)
    launcher_position = launcher_point_start.clone()

    # while lancher is inside the image...
    while is_point_hitting_rect(launcher_position, Rect((0, 0), image_size)):
        # if ray will hit the new rect...
        if _will_hit_rect_added(
            launcher_position, launcher_direction, rect_added
        ):
            # handle flag
            hitting = True

            # launch a ray
            result_ray_launched = _launch_ray(
                launcher_position,
                detection_ray_direction,
                rects,
                Rect((0, 0), image_size),
            )

            # update detected_points
            _process_ray_result(
                result_ray_launched, detected_points, launcher_direction
            )

        # if the ray launcher escapes from the new rect hitting area...
        elif hitting:
            # ...stop
            break

        # move launcher
        launcher_position += launcher_direction

    return detected_points


def _process_ray_result(
    result_ray_launched: tuple[Vector, Rect] | None,
    detected_points: list[tuple[int, int]],
    launcher_direction: Vector,
) -> None:
    """
    process the result of the ray launched.

    :param tuple[Vector, Rect]|None result_ray_launched: Result of the ray launched
    :param list[tuple[int, int]] detected_points: List of points that are detected. This will be modified.
    :param Vector launcher_direction: Direction vector of the launcher
    :rtype: None
    """

    if result_ray_launched is None:
        return

    # get the result
    detection_ray_position, _ = result_ray_launched

    # overwrite the old list
    _add_newly_found_point(
        detection_ray_position, detected_points, launcher_direction
    )


def _launch_ray(
    launching_position: Vector,
    detection_ray_direction: Vector,
    rects: Iterable[Rect],
    image_rect: Rect,
) -> tuple[Vector, Rect] | None:
    """
    Launch a detection ray from the launching position, and find the first point hits.

    This finds the frontier on the ray line. Intended to be used by `_detect_frontier_linealy()`

    :param Vector launching_position: Starting position of the ray
    :param Vector detection_ray_direction: Direction vector of the detection ray moves
    :param Iterable[Rect] rects: Rectangles that are currently putted in the magnet
    :param Rect image_rect: Rectangle of the image
    :return: If hitted -> (Position of the first point hits, Rectangle that is hitting); if not hitted -> None
    :rtype: Tuple[Vector, Rect]|None
    """
    # starting position of the ray
    # clone to avoid modifying the original vector
    detection_ray_position = launching_position.clone()

    # while detection ray is inside the image...
    while is_point_hitting_rect(detection_ray_position, image_rect):
        # check hit
        flag_hitted, hitted_rect = is_point_hitting_rects(
            detection_ray_position, rects
        )

        if flag_hitted:
            return (detection_ray_position, hitted_rect)

        # move detection ray
        detection_ray_position += detection_ray_direction

    return None


def _sort_by_direction(
    points: list[tuple[int, int]],
    direction: Vector,
) -> list[tuple[int, int]]:
    """
    Sort the points by the direction.

    :param list[tuple[int, int]] points: List of points. This won't be modified.
    :param Vector direction: Direction vector. Must be either TO_RIGHT, TO_LEFT, TO_UP, or TO_DOWN.
    :return: Sorted list of points
    :rtype: list[tuple[int, int]]
    """
    # also get components of the target direction for using bisect.bisect

    points = points.copy()

    # if direction is x-axis...
    if direction.x == 0:
        # sort by x in ascending order
        points.sort(key=lambda x: x[0])

    else:
        # sort by y in ascending order
        points.sort(key=lambda x: x[1])

    return points


def _initialize_directions(interval_x: float, interval_y: float) -> None:
    """
    Initialize the direction vectors.

    :param float interval_x: interval of the precision; x
    :param float interval_y: interval of the precision; y
    :rtype: None
    """

    global TO_RIGHT, TO_LEFT, TO_UP, TO_DOWN

    TO_RIGHT = Vector(interval_x, 0)
    TO_LEFT = Vector(-interval_x, 0)
    TO_UP = Vector(0, -interval_y)
    TO_DOWN = Vector(0, interval_y)


def _will_hit_rect_added(
    launcher_position: Vector,
    launcher_direction: Vector,
    rect_added: Rect,
) -> bool:
    """
    Check if the launcher will hit the rect_added.

    :param Vector launcher_position: Position of the launcher
    :param Vector launcher_direction: Direction vector of the launcher
    :param Rect rect_added: Rectangle that is added at the last step.
    :return: If the launcher will hit the rect_added -> True, else -> False
    :rtype: bool
    """

    if (
        # if the launcher moving vertically...
        (launcher_direction.x == 0)
        and
        # ...check y axis
        (
            rect_added.left_top[1]
            <= launcher_position.y
            <= rect_added.right_bottom[1]
        )
    ):
        # ... is hitting
        return True
    # if the launcher moving horizontally...
    # ...check x axis
    elif (
        rect_added.left_top[0]
        <= launcher_position.x
        <= rect_added.right_bottom[0]
    ):
        # ... is hitting
        return True
    else:
        # ... is not hitting
        return False


def _add_newly_found_point(
    point_found: tuple[int, int],
    frontier_points: list[tuple[int, int]],
    launcher_direction: Vector,
) -> None:
    """
    Add the newly found point to the frontier.

    :param tuple[int, int] point_found: Point found
    :param list[tuple[int, int]] frontier_points: List of points of the frontier. This will be modified.
    :param Vector launcher_direction: Direction vector of the launcher
    :rtype: None
    """

    # if the launcher moving vertically...
    if launcher_direction.x == 0:
        # find by y axis
        components = [point[1] for point in frontier_points]

        _add_newly_found_point_with_specified_component(
            components, frontier_points, point_found, point_found[1]
        )

    # if the launcher moving horizontally...
    else:
        # find by x axis
        components = [point[0] for point in frontier_points]

        _add_newly_found_point_with_specified_component(
            components, frontier_points, point_found, point_found[0]
        )


def _add_newly_found_point_with_specified_component(
    components: list[int],
    frontier_points: list[tuple[int, int]],
    point_found: tuple[int, int],
    point_component: int,
) -> None:
    """
    Update the frontier with the newly found point by _add_newly_found_point()

    :param list[int] components: List of components of the frontier points
    :param list[tuple[int, int]] frontier_points: List of points of the frontier. This will be modified.
    :param tuple[int, int] point_found: Point found
    :param int point_component: Component of the point found
    :rtype: None
    """
    index = bisect(components, point_component)

    # if there was a proceeding point...
    if (index < len(components)) and (point_component == components[index]):
        # ... overwrite
        frontier_points[index] = point_found

    # if there was no proceeding point...
    else:
        # ... newly insert

        # bisect.bisect returns the index of the point that is bigger than the target point
        frontier_points.insert(index, point_found)
