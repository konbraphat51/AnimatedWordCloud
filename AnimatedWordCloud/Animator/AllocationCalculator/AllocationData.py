# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Classes that includes the data of size and position of each words
"""

from __future__ import annotations


class AllocationInFrame:
    """
    Positions and size of each words
    """

    def __init__(self) -> None:
        """
        Prepare empty data
        """

        # word -> (font size, left-top position)
        self.words: dict[str, tuple[float, tuple[float, float]]] = {}

    def add(
        self, word: str, font_size: float, left_top: tuple[float, float]
    ) -> None:
        """
        Add a word

        :param str word: Word to add
        :param float font_size: Font size of the word
        :param tuple[float, float] left_top: Left-top position of the word
        :rtype: None
        """

        self.words[word] = (font_size, left_top)


class AllocationTimelapse:
    """
    Timelapse of positions and size of each words
    """

    def __init__(self) -> None:
        """
        Prepare empty data
        """

        # (time_name, AllocationInFrame)
        self.timelapse: list[tuple(str, AllocationInFrame)] = []

    def add(
        self, time_name: str, allocation_in_frame: AllocationInFrame
    ) -> None:
        """
        Add a frame of allocation data

        :param str time_name: Name of the time
        :param AllocationInFrame allocation_in_frame: Allocation data of the frame
        :rtype: None
        """

        self.timelapse.append((time_name, allocation_in_frame))
