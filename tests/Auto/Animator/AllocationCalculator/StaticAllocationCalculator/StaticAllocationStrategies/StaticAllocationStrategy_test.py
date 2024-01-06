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
    instance = StaticAllocationStrategy(1000, 1000)

    with raises(NotImplementedError):
        instance.allocate([], AllocationInFrame(from_static_allocation=True))

    allocation_previous = AllocationInFrame(from_static_allocation=True)
    allocation_previous.add("test", 10, (30, 10))

    allocation_current = AllocationInFrame(from_static_allocation=True)
    allocation_current.add("test1", 20, (40, 10))

    words_current = [Word("test2", 30, 30, (20, 30))]

    # test add_missing_word_to_previous_frame()
    instance.add_missing_word_to_previous_frame(
        allocation_previous, words_current
    )
    assert allocation_previous["test2"] is not None

    # test add_missing_word_from_previous_frame()
    instance.add_missing_word_from_previous_frame(
        allocation_previous, allocation_current
    )
    assert allocation_current["test"] is not None
