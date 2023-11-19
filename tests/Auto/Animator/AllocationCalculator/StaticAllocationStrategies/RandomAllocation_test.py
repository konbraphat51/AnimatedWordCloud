# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
testing RandomAllocation class
"""

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.RandomAllocation import (
    RandomAllocation,
)
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.Word import (
    Word,
)


def test_RandomAllocation():
    words = [
        Word("test", 1, 10, (30, 10)),
        Word("test", 3, 30, (20, 30)),
        Word("test", 4, 40, (40, 40)),
    ]

    instance = RandomAllocation(100, 100)
    assert instance.allocate(words) is not None
