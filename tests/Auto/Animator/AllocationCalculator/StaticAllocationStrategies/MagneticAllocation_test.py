# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
testing MagneticAllocation module
"""

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.MagneticAllocation import (
    MagneticAllocation,
    MagnetOuterFrontier,
)
from AnimatedWordCloud.Animator import AllocationInFrame
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    Word,
)


def test_MagneticOuterFrontier():
    instance = MagnetOuterFrontier()
    assert instance.from_up == []
    assert instance.from_down == []
    assert instance.from_left == []
    assert instance.from_right == []


def test_MagneticAllocation():
    instance = MagneticAllocation(1000, 1000, 10)

    allocation_previous = AllocationInFrame()
    allocation_previous.add("test", 10, (30, 10))

    words = [
        Word("test", 1, 10, (30, 10)),
        Word("test2", 3, 30, (20, 30)),
    ]

    assert instance.allocate(words, allocation_previous) is not None
