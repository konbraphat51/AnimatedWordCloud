# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
testing the AnimatedWordCloud module
"""

from AnimatedWordCloud.Animator.AllocationCalculator.AllocationData import (
    AllocationInFrame,
    AllocationTimelapse,
)


def test_AllocationInFrame():
    instance = AllocationInFrame()

    # test add + getitem
    instance.add("test", 10, (0, 0))
    instance.add("test2", 20, (10, 10))
    assert instance["test"] == (10, (0, 0))

    # test setitem
    instance["test3"] = (20, (0, 0))
    assert instance["test3"] == (20, (0, 0))


def test_AllocationTimelapse():
    instance = AllocationTimelapse()

    # test add + getitem
    instance.add(0, AllocationInFrame())
    instance.add(1, AllocationInFrame())
    assert instance.get_frame(0) is not None
