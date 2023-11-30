# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Base class for static allocation strategies
"""

from typing import Iterable
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.RandomAllocation import (
    put_randomly,
)
from AnimatedWordCloud.Utils import Word, AllocationInFrame


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

    def add_missing_word_to_previous_frame(
        self, frame_previous: AllocationInFrame, words_current: Iterable[Word]
    ) -> None:
        """
        Add word in instance of the previous frame

        Find words going to be putted in current frame
            but not in previous frame.
        Add the missing words randomly put the word in the previous frame.
        The putting algorithm is the same as the one in `RandomAllocation`.
        This is intended to let appearing words appear smoothly.

        :param AllocationInFrame frame_previous:
            The allocation data of the previous frame
        :param Iterable[Word] words_current:
            The words to be putted in the current frame
        :rtype: None
        """

        # find missing words
        words_previous = set(frame_previous.words.keys())
        word_texts_current = []
        words_size = {}
        words_font_size = {}
        for word in words_current:
            if word.text not in words_current:
                word_texts_current.append(word.text)
                words_size[word.text] = word.text_size
                words_font_size[word.text] = word.font_size
        missing_words = set(word_texts_current) - words_previous

        # add missing words
        for word in missing_words:
            # put randomly
            text_lefttop_position = put_randomly(
                self.image_width, self.image_height, words_size[word]
            )

            # allocate in the output
            frame_previous.add(
                word, words_font_size[word], text_lefttop_position
            )

    def add_missing_word_from_previous_frame(
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
            estimated_size = (
                len(word) * frame_previous[word][0],
                frame_previous[word][0],
            )
            lefttop_position = put_randomly(
                self.image_width, self.image_height, estimated_size
            )
            frame_current.add(word, frame_previous[word][0], lefttop_position)
