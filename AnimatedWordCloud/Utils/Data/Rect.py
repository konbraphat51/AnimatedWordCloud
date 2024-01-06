# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Handling rect in static allocation strategies
"""

from __future__ import annotations


class Rect:
    """
    Data of rectangle in static allocation strategies
    """

    def __init__(
        self, left_top: tuple[int, int], right_bottom: tuple[int, int]
    ) -> None:
        """
        :param Tuple[int,int] left_top: Left top position of the rect
        :param Tuple[int,int] right_bottom: Right bottom position of the rect
        """
        self.left_top = left_top
        self.right_bottom = right_bottom
