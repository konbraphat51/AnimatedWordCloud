# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Base class for static allocation strategies
"""

from collections.abc import Iterable
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    Word,
)
from AnimatedWordCloud.Animator import AllocationInFrame
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.RandomAllocation import (
    put_randomly,
)


class StaticAllocationStrategy:
    """
    Base class for static allocation strategies
    """

    def __init__(
        self,
        image_width: int,
        image_height: int,
    ):
        self.image_width = image_width
        self.image_height = image_height

    def allocate(
        self, words: Iterable[Word], allocation_before: AllocationInFrame
    ) -> AllocationInFrame:
        """
        Allocate the words

        This is abstract method.

        :param Iterable[Word] words: The words to allocate
        :param AllocationInFrame allocation_before: The allocation data of the previous frame
        """

        raise NotImplementedError

    def add_word_in_previous_frame(
        self, frame_previous: AllocationInFrame, word: Word
    ) -> None:
        """
        Add word in instance of the previous frame

        Randomly put the word in the previous frame.
        The putting algorithm is the same as the one in `RandomAllocation`.

        :param AllocationInFrame frame_previous:
            The allocation data of the previous frame
        :rtype: None
        """

        # put
        text_lefttop_position = put_randomly(
            self.image_width, self.image_height, word
        )

        # allocate in the output
        frame_previous[word.text] = (word.font_size, text_lefttop_position)

    def add_missing_word(
        self,
        frame_previous: AllocationInFrame,
        frame_current: AllocationInFrame,
    ) -> None:
        """
        Add missing word from the previous frame
            to the instance of the current frame

        Find words existed in previous frame but not in current,
            and add them to the current frame.
        Added words are putted randomly, same as `RandomAllocation`.
        This must be called after all words are allocated in the current frame.
        This is intended to let disappearing words disappear smoothly.

        :param AllocationInFrame frame_previous:
            The allocation data of the previous frame
        :param AllocationInFrame frame_current:
            The allocation data of the current frame
        :rtype: None
        """

        # find missing words
        words_previous = set(frame_previous.words.keys())
        words_current = set(frame_current.words.keys())
        words_missing = words_previous - words_current

        # add missing words
        for word in words_missing:
            lefttop_position = put_randomly(
                self.image_width, self.image_height, word
            )
            frame_current.add(
                word, (frame_previous[word][0], lefttop_position)
            )
