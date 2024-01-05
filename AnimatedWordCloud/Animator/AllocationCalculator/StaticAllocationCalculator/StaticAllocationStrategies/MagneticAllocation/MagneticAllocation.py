# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
One strategy to allocate words in static time.

First, put the largest word in the center.
Regard this word as a magnet.
Then, put the next largest word at empty point, contacting with the magnet at the center.
The point will be evaluated by evaluate_position(), and the most best point will be selected.
Repeating this process, all words will be allocated.
"""

from __future__ import annotations
import math
from typing import Iterable
from tqdm import tqdm
import joblib
from AnimatedWordCloud.Utils import (
    is_rect_hitting_rects,
    AllocationInFrame,
    Vector,
    Rect,
    Word,
)
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.StaticAllocationStrategy import (
    StaticAllocationStrategy,
)
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.MagneticAllocation.MagnetOuterFrontier import (
    MagnetOuterFrontier,
    get_magnet_outer_frontier,
)


class MagneticAllocation(StaticAllocationStrategy):
    def __init__(
        self,
        image_width: int,
        image_height: int,
        image_division: int = 100,
        verbosity: str = "none",
    ):
        """
        Initialize allocation settings
        """
        super().__init__(image_width, image_height)

        self.image_division = image_division

        self.interval_x = self.image_width / self.image_division
        self.interval_y = self.image_height / self.image_division

        self.verbosity = verbosity

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

        # missing word for previous frame
        self.add_missing_word_to_previous_frame(allocation_before, words)

        output = AllocationInFrame(from_static_allocation=True)
        magnet_outer_frontier = MagnetOuterFrontier()

        # Word rectangles that are currenly putted at the outermost of the magnet
        self.rects = set()

        # put the first word at the center
        self.center = (self.image_width / 2, self.image_height / 2)
        first_word = self.words[0]
        first_word_position = (
            self.center[0] - first_word.text_size[0] / 2,
            self.center[1] - first_word.text_size[1] / 2,
        )

        # register the first word
        rect_adding = Rect(
            first_word_position,
            (
                first_word_position[0] + first_word.text_size[0],
                first_word_position[1] + first_word.text_size[1],
            ),
        )
        self.rects.add(rect_adding)
        output.add(first_word.text, first_word.font_size, first_word_position)

        # verbose for iteration
        if self.verbosity == "debug":
            print("MagneticAllocation: Start iteration...")
            iterator = tqdm(self.words[1:])
        else:
            iterator = self.words[1:]

        # from second word
        for word in iterator:
            # get outer frontier of the magnet
            # The position candidates will be selected from this frontier
            magnet_outer_frontier = get_magnet_outer_frontier(
                self.rects,
                self.image_width,
                self.image_height,
                self.interval_x,
                self.interval_y,
                rect_adding,
                magnet_outer_frontier,
            )

            # find the best left-top position
            position = self._find_best_position(
                word,
                magnet_outer_frontier,
                self.allocations_before[word.text][1],
            )

            # update for next iteration
            rect_adding = Rect(
                position,
                (
                    position[0] + word.text_size[0],
                    position[1] + word.text_size[1],
                ),
            )

            # register rect
            self.rects.add(rect_adding)

            # register to output
            output.add(word.text, word.font_size, position)

        # add missing words for this frame
        self.add_missing_word_from_previous_frame(allocation_before, output)

        return output

    def _evaluate_position(
        self, position_from: tuple[int, int], position_to: tuple[int, int]
    ) -> float:
        """
        Evaluate the position the word beginf to put

        :param tuple[int,int] position_from:
            Position of the center of the word comming from
        :param tuple[int,int] position_to:
            Position of the center of the word going to be putted
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

        # the larger, the better; This need manual adjustment
        # adjust the coefficient mannually by visual testing

        # log(distance_movement): more important when near, not when fat
        return (
            -math.log(0.05 * distance_movement + 0.1)
            - 1.0 * distance_center**2
        )

    def _find_best_position(
        self,
        word: Word,
        magnet_outer_frontier: MagnetOuterFrontier,
        position_from: tuple[int, int],
    ) -> tuple[int, int]:
        """
        Find the best position to put the word

        Find the best position to put the word in the `magnet_outer_frontier`.
        The positions will be evaluated by `evaluate_position()`, and the best scored position will be returned.

        :param Word word: Word to put
        :param MagnetOuterFrontier magnet_outer_frontier:
            Outer frontier of the magnet at the center
        :param tuple[int,int] position_from:
            Position of the center of the word comming from
        :return: Best left-top position to put the word
        :rtype: tuple[int,int]
        """

        # + interval for a buffer for the collision detection
        # if not, this might get into the word's rects
        x_half = word.text_size[0] / 2 + self.interval_x
        y_half = word.text_size[1] / 2 + self.interval_y

        # Prepare for iteration
        pivots_to_center_list = [
            # from lower
            [
                Vector(0, y_half),
            ],
            # from top
            [
                Vector(0, -y_half),
            ],
            # from left
            [
                Vector(-x_half, 0),
            ],
            # from right
            [
                Vector(x_half, 0),
            ],
        ]

        frontier_sides = [
            magnet_outer_frontier.from_down,
            magnet_outer_frontier.from_up,
            magnet_outer_frontier.from_left,
            magnet_outer_frontier.from_right,
        ]

        # get center position candidates
        results_by_sides = joblib.Parallel(n_jobs=-1, verbose=0)(
            joblib.delayed(self._get_candidates_from_one_side)(
                pivots_to_center_list[cnt], frontier_sides[cnt]
            )
            for cnt in range(4)
        )
        center_position_candidates = []
        for results_by_side in results_by_sides:
            center_position_candidates.extend(results_by_side)

        # error handling: too small image area that cannot put the word anywhere anymore
        if len(center_position_candidates) == 0:
            raise Exception(
                "No available position found. Try to reduce font size or expand image size."
            )

        # find the best position
        best_position = self._try_put_all_candidates(
            center_position_candidates, word.text_size, position_from
        )

        # to left-top position
        best_position_left_top = (
            best_position[0] - word.text_size[0] / 2,
            best_position[1] - word.text_size[1] / 2,
        )

        return best_position_left_top

    def _get_candidates_from_one_side(
        self,
        pivots_to_center: Iterable[Vector],
        points_on_side: Iterable[Vector],
    ) -> list[tuple[int, int]]:
        """
        Get all candidates of the center position from one side

        Intended to be used in `find_best_position()`

        :param Iterable[Vector] pivots_to_center:
            Vector of  (center of the word) - (pivot)
        :param Iterable[Vector] points_on_side:
            Points on the side
        :return: Candidates of the center position
        :rtype: list[tuple[int, int]]
        """

        # get all candidate center positions
        candidates = []
        for point_on_side in points_on_side:
            for pivot_to_center in pivots_to_center:
                candidates.append(point_on_side + pivot_to_center)

        return candidates

    def _try_put_all_candidates(
        self,
        center_positions: Iterable[tuple[int, int]],
        size: tuple[int, int],
        position_from: tuple[int, int],
    ) -> tuple[int, int]:
        """
        Try to put the word at the gived place and evaluate the score, and return the best scored position

        :param Iterable[tuple[int,int]] center_positions:
            Candidate list of center points of the word
        :param tuple[int,int] size: Size of the word
        :param tuple[int,int] position_from:
            Position of the center of the word comming from
        :return: Best center position
        :rtype: tuple[int, int]
        """

        results_evaluation = joblib.Parallel(n_jobs=-1, verbose=0)(
            joblib.delayed(self._try_put_position)(
                center_position, size, position_from
            )
            for center_position in center_positions
        )

        # find best score
        best_position = None
        best_score = -float("inf")
        for cnt, result_evaluation in enumerate(results_evaluation):
            if (result_evaluation is not None) and (
                result_evaluation > best_score
            ):
                best_score = result_evaluation
                best_position = center_positions[cnt]

        # guard
        if best_position is None:
            raise Exception("No position found")

        return best_position

    def _is_hitting_other_words(
        self,
        center_position: tuple[int, int] | Vector,
        size: tuple[int, int] | Vector,
    ) -> bool:
        """
        Check if the given rect is hitting with other words

        :param tuple[int,int] | Vector center_position: Center point of the word
        :param tuple[int,int] | Vector size: Size of the word
        :return: True if the center point is hitting with other words
        :rtype: bool
        """
        # ensure to Vector
        if center_position.__class__ == tuple:
            center_position = Vector(center_position)
        if size.__class__ == tuple:
            size = Vector(size)

        left_top = center_position - size / 2
        right_bottom = center_position + size / 2

        return is_rect_hitting_rects(
            Rect(
                left_top.convert_to_tuple(),
                right_bottom.convert_to_tuple(),
            ),
            self.rects,
        )

    def _try_put_position(
        self,
        center_position: tuple[float, float],
        size: tuple[float, float],
        position_from: tuple[float, float],
    ) -> float:
        """
        Evaluate the position the word if putted

        :param tuple[float,float] center_position: Position of the center of the word
        :param tuple[float,float] size: Size of the word
        :param tuple[float,float] position_from: Position of the center of the word comming from
        :return: Evaluation score. Smaller is the better
        :rtype: float
        """

        # if hitting with other word...
        if self._is_hitting_other_words(center_position, size):
            # ...skip this position
            return None

        score = self._evaluate_position(position_from, center_position)

        return score
