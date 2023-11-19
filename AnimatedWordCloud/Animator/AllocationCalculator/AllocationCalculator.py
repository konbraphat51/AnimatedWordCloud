# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Calculate positions and size of words during each frame
"""

from typing import List
from AnimatedWordCloud import TimelapseWordVector
from AnimatedWordCloud.Animator import AllocationInFrame


def calculate(
    word_vector_timelapse: TimelapseWordVector,
) -> List[AllocationInFrame]:
    """
    Calculate positions and size of words during each frame

    :param TimelapseWordVector word_vector_timelapse:
    :return: Position/size data of each video frame
    :rtype: List[PositionInFrame]
    """

    raise NotImplementedError()
