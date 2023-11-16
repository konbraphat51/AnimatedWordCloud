# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Calculate positions and size of words during each frame
"""

from typing import List, Dict, Tuple
from AnimatedWordCloud import TimelapseWordVector


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


def calculate(
    word_vector_timelapse: TimelapseWordVector,
) -> List[AllocationInFrame]:
    """
    Calculate positions and size of words during each frame

    :param TimelapseWordVector word_vector_timelapse:
    :return: Position/size data of each video frame
    :rtype: List[PositionInFrame]
    """

    return word_vector_timelapse
