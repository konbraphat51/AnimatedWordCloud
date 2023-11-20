# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
testing MagnetOuterFrontier module
"""

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.MagneticAllocation import (
    MagnetOuterFrontier,
    get_magnet_outer_frontier,
)
from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies import (
    Rect,
    is_point_hitting_rect,
)


def test_MagneticOuterFrontier():
    instance = MagnetOuterFrontier()
    assert instance.from_up == []
    assert instance.from_down == []
    assert instance.from_left == []
    assert instance.from_right == []


def test_get_magnet_outer_frontier():
    rect = Rect((30, 30), (50, 50))
    frontier, _ = get_magnet_outer_frontier([rect], 100, 100, 10)

    assert is_point_hitting_rect(frontier.from_up[1], rect)
