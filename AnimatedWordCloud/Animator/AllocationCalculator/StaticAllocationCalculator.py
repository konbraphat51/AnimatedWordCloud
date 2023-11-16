# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Calculate allocation of each words in each static time
"""

from AnimatedWordCloud import WordVector, TimelapseWordVector
from AnimatedWordCloud.Animator import AllocationInFrame, AllocationTimelapse

def allocate(word_vector: WordVector) -> AllocationInFrame:
    """
    Calculate allocation of each words in each static time

    :param WordVector word_vector: The word vector
    :return: Allocation data of the frame
    :rtype: AllocationInFrame
    """
    
def allocate_all(timelapse: TimelapseWordVector) -> AllocationTimelapse:
    """
    Calculate allocation of each words in several each static time

    :param TimelapseWordVector timelapse: The word vector    
    :return: Allocation data of each frame
    :rtype: AllocationTimelapse
    """
    
    times = len(timelapse)

    allocation_timelapse = AllocationTimelapse()
    
    for cnt in range(times):
        allocation = allocate(timelapse[cnt].word_vector)
        allocation_timelapse.add(timelapse[cnt].time_name, allocation)
        
    return allocation_timelapse