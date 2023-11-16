# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Classes that includes the data of size and position of each words
"""

from typing import Dict, Tuple


class AllocationInFrame:
    """
    Positions and size of each words
    """

    def __init__(self) -> None:
        """
        Prepare empty data
        """

        # word -> (size, position)
        self.words: Dict[str, Tuple[float, Tuple[float, float]]] = {}
