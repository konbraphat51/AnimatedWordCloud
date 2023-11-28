# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
testing RandomAllocation class
"""

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.RandomAllocation import (
    allocate_randomly,
    put_randomly,
    Word,
)


def test_RandomAllocation():
    words = [
        Word("test", 1, 10, (30, 10)),
        Word("test", 3, 30, (20, 30)),
        Word("test", 4, 40, (40, 40)),
    ]

    assert allocate_randomly(words, 100, 100) is not None


def test_put_randomly():
    assert put_randomly(100, 100, (10, 10)) is not None
