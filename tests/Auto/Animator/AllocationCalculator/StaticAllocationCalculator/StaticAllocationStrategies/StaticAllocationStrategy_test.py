# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
testing StaticAllocationStrategy class
"""

from pytest import raises
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.StaticAllocationStrategy import (
    StaticAllocationStrategy,
    Word,
    AllocationInFrame,
)


def test_StaticAllocationStrategy():
    instance = StaticAllocationStrategy(100, 100)

    with raises(NotImplementedError):
        instance.allocate([], AllocationInFrame())

    allocation_previous = AllocationInFrame()
    allocation_previous.add("test", 10, (30, 10))

    allocation_current = AllocationInFrame()
    allocation_current.add("test1", 20, (40, 10))

    words_current = [Word("test2", 30, 30, (20, 30))]

    assert (
        instance.handle_missing_words(
            allocation_previous, allocation_current, words_current
        )
        is None
    )
