# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
testing MagneticAllocation module
"""

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.MagneticAllocation.MagneticAllocation import (
    MagneticAllocation,
    AllocationInFrame,
    Word,
    Config
)


def test_MagneticAllocation():
    config = Config(image_width=1000, image_height=1000, image_division=200)
    instance = MagneticAllocation(config)

    allocation_previous = AllocationInFrame(from_static_allocation=True)
    allocation_previous.add("test", 10, (30, 10))
    allocation_previous.add("test1", 30, (20, 30))

    words = [
        Word("test", 1, 10, (30, 10)),
        Word("test2", 3, 30, (20, 30)),
    ]

    assert instance.allocate(words, allocation_previous) is not None
