# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
GPU accelerated version of the Magnetic Allocation strategy.
"""

from typing import Iterable
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.MagneticAllocation.MagneticAllocation import (
    MagneticAllocation
)
from AnimatedWordCloud.Utils import Vector

class MagneticAllocationGPU(MagneticAllocation):
    """
    GPU accelerated version of the Magnetic Allocation strategy.
    """

    def __init__(self, wordcloud, **kwargs):
        super().__init__(wordcloud, **kwargs)

        
        