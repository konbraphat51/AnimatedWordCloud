# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Handful class of containing timelapse data of word vectors.
"""

from __future__ import annotations
from typing import Dict, Tuple, List
from collections.abc import Iterable
import heapq


class WordVector:
    """
    Contains each word's weight
    """

    def __init__(self) -> None:
        """
        Prepare empty data
        """

        # use heap to easily get the rankings
        # to order by weight,
        #   the weight must be the first element of the tuple
        # but the output must be the word first
        self._word_heap: List[Tuple[float, str]] = []

        # also prepare a dictionary for direct access to word
        self._word_dictionary: Dict[str, float] = {}
        

    def add(self, word: str, weight: float) -> None:
        """
        Add a word to the data

        :param str word: The word
        :param float weight: The weight of the word
        :rtype: None
        """

        heapq.heappush(self._word_heap, (weight, word))
        self._word_dictionary[word] = weight


    def add_multiple(self, word_weights: Iterable[Tuple[str, float]]) -> None:
        """
        Add multiple words to the data

        :param Iterable[Tuple[str, float]] word_weight: The words and their weights
        :rtype: None
        """

        for word, weight in word_weights:
            self.add(word, weight)

    def get_ranking(self, start: int, end: int) -> List[Tuple(str, float)]:
        """
        Get the ranking of the words

        This is simply a slice of the heap.

        :param int start: Start of the ranking.
        :param int end: End of the ranking. This index will not included. (such as list slice)
        If -1, to the last.
        :return: The ranking of the words
        :rtype: List[Tuple(str, float)]
        """

        return [(tup[1], tup[0]) for tup in self._word_heap[start:end]]

    def get_weight(self, word: str) -> float:
        """
        Get the weight of the word

        :param str word: The word
        :return: The weight of the word
        :rtype: float
        """
        return self._word_dictionary[word]
    
    def convert_from_dict(word_weights: Dict[str, float]) -> WordVector:
        """
        Convert from a dictionary of word and weight to WordVector instance.

        This is static conversion method.

        :param Dict[str, float] word_weights: The words and their weights
        :return: The WordVector instance
        :rtype: WordVector
        """

        instance = WordVector()

        for word, weight in word_weights.items():
            instance.add(word, weight)

        return instance


class TimeFrame:
    """
    A single time frame of word vector
    """

    def __init__(self, time_name: str, word_vector: WordVector) -> None:
        """
        Prepare the time frame

        :param str time_name: Name of the time
        :param WordVector word_vector: Word vector
        """

        self.time_name: str = time_name
        self.word_vector: WordVector = word_vector
        
    def convert_from_dict(time_name: str, word_weights: Dict[str, float]) -> TimeFrame:
        """
        Convert from a dictionary of word and weight to TimeFrame instance.

        This is static conversion method.

        :param str time_name: Name of the time
        :param Dict[str, float] word_weights: The words and their weights
        :return: The TimeFrame instance
        :rtype: TimeFrame
        """

        word_vector = WordVector.convert_from_dict(word_weights)

        return TimeFrame(time_name, word_vector)

    def convert_from_tup_dict(data: Iterable[str, Dict[str, float]]):
        """
        Convert from a dictionary of word and weight to TimeFrame instance.

        This is static conversion method.

        :param Iterable[str, Dict[str, float]] data: The words and their weights
        :return: The TimeFrame instance
        :rtype: TimeFrame
        """

        return TimeFrame.convert_from_dict(data[0], data[1])

class TimelapseWordVector:
    """
    Timelapse data of word vectors.

    The data structure is a list of TimeFrame
    """

    def __init__(self) -> None:
        """
        Prepare empty data
        """

        # main data
        self.timeframes: List[TimeFrame] = []

    def __getitem__(self, index: int) -> TimeFrame:
        """
        Returns the item at the given index

        :param int index: The index
        :return: The timeframe at the given index
        :rtype: TimeFrame
        """
        return self.timeframes[index]

    def __len__(self) -> int:
        """
        Returns the length of the timelapse data

        :return: The length of the timelapse data
        :rtype: int
        """
        return len(self.timeframes)

    def add_time_frame(self, timeframe: TimeFrame) -> None:
        """
        Add a time frame to the timelapse data

        :param str time_name: Name of the time
        :param Dict[str, float] word_vector: Word vector
        :rtype: None
        """

        self.timeframes.append(timeframe)
