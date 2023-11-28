# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Data class contains attributes of each words
"""

from __future__ import annotations


class Word:
    """
    Data class contains attributes of each words.
    This is used to contact with allocation strategies.
    """

    def __init__(
        self,
        text: str,
        weight: float,
        font_size: int,
        text_size: tuple[int, int],
    ):
        self.text = text
        self.weight = weight
        self.font_size = font_size
        self.text_size = text_size
