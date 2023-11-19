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

from __future__ import annotations
from collections.abc import Iterable
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    Word,
)
from AnimatedWordCloud.Animator import AllocationInFrame
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies import (
    Rect,
    is_point_hitting_rects,
    StaticAllocationStrategy,
    is_rect_hitting_rects,
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
        self.from_up: list[tuple[int, int]] = []
        self.from_down: list[tuple[int, int]] = []
        self.from_left: list[tuple[int, int]] = []
        self.from_right: list[tuple[int, int]] = []


class MagneticAllocation(StaticAllocationStrategy):
    def __init__(
        self, image_width: int, image_height: int, image_division: int = 100
    ):
        super().__init__(image_width, image_height)
        self.image_division = image_division

    def allocate(
        self, words: Iterable[Word], allocation_before: AllocationInFrame
    ) -> AllocationInFrame:
        """
        Allocate words in magnetic strategy

        :param Iterable[Word] words: Words to allocate. Order changes the result.
        :param AllocationInFrame allocation_before: Allocation data at one static frame before
        :return: Allocation data of the frame
        :rtype: AllocationInFrame
        """

        self.words = words
        self.allocations_before = allocation_before

        output = AllocationInFrame()

        # Word rectangles that are currenly putted
        #   at the oytermost of the magnet
        self.rects_outermost = set()

        # put the first word at the center
        self.center = (self.image_width / 2, self.image_height / 2)
        first_word = self.words[0]
        first_word_position = (
            self.center[0] - first_word.text_size[0] / 2,
            self.center[1] - first_word.text_size[1] / 2,
        )

        # register
        self.rects_outermost.add(
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
        for word in self.words[1:]:
            magnet_outer_frontier = self.get_magnet_outer_frontier()

            # find the best left-top position
            position = self.find_best_position(
                word,
                magnet_outer_frontier,
                self.allocations_before[word.text][1],
            )

            # register rect
            self.rects_outermost.add(
                Rect(
                    position,
                    (
                        position[0] + word.text_size[0],
                        position[1] + word.text_size[1],
                    ),
                )
            )

            # register to output
            output.add(word.text, word.font_size, position)

        return output

    def get_magnet_outer_frontier(self) -> MagnetOuterFrontier:
        """
        Find the outer frontier of the magnet at the center

        :return: Outer frontier of the magnet at the center
        :rtype: MagnetOuterFrontier
        """

        X_INTERVAL = self.image_width / self.image_division
        Y_INTERVAL = self.image_height / self.image_division

        current_hitted_rects = set()

        magnet_outer_frontier = MagnetOuterFrontier()

        # from up
        for x in range(1, self.image_width, X_INTERVAL):
            for y in range(0, self.image_height + 1, Y_INTERVAL):
                flag_hitted, hitted_rect = is_point_hitting_rects(
                    (x, y), self.rects_outermost
                )
                if flag_hitted:
                    current_hitted_rects.add(hitted_rect)
                    magnet_outer_frontier.from_up.append((x, y))
                    break

        # from down
        for x in range(1, self.image_width, X_INTERVAL):
            for y in range(self.image_height, -1, -Y_INTERVAL):
                flag_hitted, hitted_rect = is_point_hitting_rects(
                    (x, y), self.rects_outermost
                )
                if flag_hitted:
                    current_hitted_rects.add(hitted_rect)
                    magnet_outer_frontier.from_down.append((x, y))
                    break

        # from left
        for y in range(1, self.image_height, Y_INTERVAL):
            for x in range(0, self.image_width + 1, X_INTERVAL):
                flag_hitted, hitted_rect = is_point_hitting_rects(
                    (x, y), self.rects_outermost
                )
                if flag_hitted:
                    current_hitted_rects.add(hitted_rect)
                    magnet_outer_frontier.from_left.append((x, y))
                    break

        # from right
        for y in range(1, self.image_height, Y_INTERVAL):
            for x in range(self.image_width, -1, -X_INTERVAL):
                flag_hitted, hitted_rect = is_point_hitting_rects(
                    (x, y), self.rects_outermost
                )
                if flag_hitted:
                    current_hitted_rects.add(hitted_rect)
                    magnet_outer_frontier.from_right.append((x, y))
                    break

        # update rects_outermost
        self.rects_outermost = current_hitted_rects

        return magnet_outer_frontier

    def evaluate_position(
        self, position_from: tuple[int, int], position_to: tuple[int, int]
    ) -> float:
        """
        Evaluate the position the word beginf to put

        :param tuple[int,int] position_from: Position of the center of the word comming from
        :param tuple[int,int] position_to: Position of the center of the word going to be putted
        :param tuple[int,int] center: Position of the center of the magnet
        :return: Evaluation value. Smaller is the better
        """

        distance_movement = math.sqrt(
            (position_from[0] - position_to[0]) ** 2
            + (position_from[1] - position_to[1]) ** 2
        )

        distance_center = math.sqrt(
            (position_to[0] - self.center[0]) ** 2
            + (position_to[1] - self.center[1]) ** 2
        )

        # the smaller, the better; This need manual adjustment
        return distance_movement**2 + distance_center**2

    def find_best_position(
        self,
        word: Word,
        magnet_outer_frontier: MagnetOuterFrontier,
        position_from: tuple[int, int],
    ) -> tuple[int, int]:
        """
        Find the best position to put the word

        Find the best position to put the word in the `magnet_outer_frontier`.
        The positions will be evaluated by `evaluate_position()`,
            and the best scored position will be returned.

        :param Word word: Word to put
        :param MagnetOuterFrontier magnet_outer_frontier: Outer frontier of the magnet at the center
        :param tuple[int,int] position_from: Position of the center of the word comming from
        :return: Best left-top position to put the word
        :rtype: tuple[int,int]
        """

        x_half = word.text_size[0] / 2
        y_half = word.text_size[1] / 2
        left_bottom_to_center = (x_half, -y_half)
        right_bottom_to_center = (-x_half, -y_half)
        left_top_to_center = (x_half, y_half)
        right_top_to_center = (-x_half, y_half)

        # from upper of the magnet
        pivots_to_center = [
            left_bottom_to_center,
            (0, -y_half),
            right_bottom_to_center,
        ]
        best_from_up = self.put_on_one_side(
            pivots_to_center,
            word.text_size,
            magnet_outer_frontier.from_up,
            position_from,
        )

        # from lower of the magnet
        pivots_to_center = [
            left_top_to_center,
            (0, y_half),
            right_top_to_center,
        ]
        best_from_down = self.put_on_one_side(
            pivots_to_center,
            word.text_size,
            magnet_outer_frontier.from_down,
            position_from,
        )

        # from left of the magnet
        pivots_to_center = [
            right_bottom_to_center,
            (x_half, 0),
            right_top_to_center,
        ]
        best_from_left = self.put_on_one_side(
            pivots_to_center,
            word.text_size,
            magnet_outer_frontier.from_left,
            position_from,
        )

        # from right of the magnet
        pivots_to_center = [
            left_bottom_to_center,
            (-x_half, 0),
            left_top_to_center,
        ]
        best_from_right = self.put_on_one_side(
            pivots_to_center,
            word.text_size,
            magnet_outer_frontier.from_right,
            position_from,
        )

        # conclude the best position
        best_position = None
        best_score = None
        for position, score in [
            best_from_up,
            best_from_down,
            best_from_left,
            best_from_right,
        ]:
            if best_score is None or score < best_score:
                best_position = position
                best_score = score

        # to left-top
        best_position = (
            best_position[0] - x_half,
            best_position[1] - y_half,
        )

        return best_position

    def put_on_one_side(
        self,
        pivots_to_center: Iterable[tuple[int, int]],
        size: tuple[int, int],
        points_on_side: Iterable[tuple[int, int]],
        position_from: tuple[int, int],
    ) -> tuple[tuple[int, int], float]:
        """
        Try to put on one side of the magnet,
            and find the best position on that side

        Put all pivots on the each point on the side,
            and find the best position by `evaluate_position()`.

        :param Iterable[tuple[int,int]] pivots_to_center: Vector of  (center of the word) - (pivot)
        :param tuple[int,int] size: Size of the word
        :param Iterable[tuple[int,int]] points_on_side: Points on the side
        :param tuple[int,int] position_from: Position of the center of the word comming from
        :return: (Best position, Best score)
        :rtype: tuple[tuple[int,int], float]
        """

        best_position = None
        best_score = None

        for point_on_side in points_on_side:
            for pivot_to_center in pivots_to_center:
                # try put the pivot on the point
                center_position = (
                    point_on_side[0] + pivot_to_center[0],
                    point_on_side[1] + pivot_to_center[1],
                )

                # if hitting with other word...
                if is_rect_hitting_rects(
                    Rect(
                        # left_top
                        (
                            center_position[0] - size[0] / 2,
                            center_position[1] - size[1] / 2,
                        ),
                        # right_bottom
                        (
                            center_position[0] + size[0] / 2,
                            center_position[1] + size[1] / 2,
                        ),
                    ),
                    self.rects_outermost,
                ):
                    # ...skip this position
                    continue

                score = self.evaluate_position(position_from, center_position)

                if best_score is None or score < best_score:
                    best_position = center_position
                    best_score = score

        return (best_position, best_score)
