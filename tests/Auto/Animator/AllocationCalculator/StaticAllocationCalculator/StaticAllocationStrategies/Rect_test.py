# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Testing the Rect module
"""

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.Rect import *


def test_Rect():
    instance = Rect((0, 0), (100, 100))

    assert instance.left_top == (0, 0)
    assert instance.right_bottom == (100, 100)


def test_collisions():
    rect0 = Rect((0, 0), (100, 100))
    rect1 = Rect((75, 75), (150, 150))
    rect2 = Rect((150, 150), (250, 250))

    point0 = (50, 50)
    point1 = (150, 150)
    point2 = (300, 300)

    assert is_point_hitting_rect(point0, rect0)
    assert is_point_hitting_rect(point1, rect1)
    assert not is_point_hitting_rect(point2, rect2)

    assert is_point_hitting_rects(point0, [rect0, rect1])[0]
    assert is_point_hitting_rects(point1, [rect0, rect1])[1].left_top == (
        75,
        75,
    )
    assert not is_point_hitting_rects(point2, [rect0, rect1])[0]

    assert is_rect_hitting_rect(rect0, rect1)
    assert not is_rect_hitting_rect(rect0, rect2)

    assert is_rect_hitting_rects(rect0, [rect1, rect2])
    assert not is_rect_hitting_rects(rect0, [rect2])
