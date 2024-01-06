# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
testing the AnimatedWordCloud module
"""

from AnimatedWordCloud.Utils import (
    AllocationInFrame,
    AllocationTimelapse,
)


def test_AllocationInFrame():
    instance = AllocationInFrame(from_static_allocation=True)

    # test add + getitem
    instance.add("test", 10, (0, 0))
    instance.add("test2", 20, (10, 10))
    assert instance["test"] == (10, (0, 0))


def test_AllocationTimelapse():
    instance = AllocationTimelapse()

    # test add + getitem
    instance.add(0, AllocationInFrame(from_static_allocation=True))
    instance.add(1, AllocationInFrame(from_static_allocation=True))
    assert instance.get_frame(0) is not None
