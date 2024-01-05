# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Calculate positions and size of words during each frame
"""

from typing import List
from AnimatedWordCloud.Utils import AllocationTimelapse, TimelapseWordVector
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import allocate_all as allocate_static
from AnimatedWordCloud.Animator.AllocationCalculator.AnimatetdAllocationCalculator import animated_allocate

def calculate(
    word_vector_timelapse: TimelapseWordVector,
) -> AllocationTimelapse:
    """
    Calculate positions and size of words during each frame
    
    This will call
    - StaticAllocationCalculator: Calculate positions and size of words in each frame
    - AnimatedAllocationCalculator: Calculate the motion of each word in between the static frames

    :param TimelapseWordVector word_vector_timelapse:
    :return: timelapse of calculated allocation
    :rtype: AllocationTimelapse
    """

    # Calculate static allocation
    static_allocation_timelapse = allocate_static(word_vector_timelapse)

    # Calculate animated allocation
    animated_allocation_timelapse = animated_allocate(
        static_allocation_timelapse
    )

    return animated_allocation_timelapse
