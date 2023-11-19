# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Testing the StaticAllocationCalculator module
"""


from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator import (
    calculate_font_size,
    estimate_text_size,
)
from AnimatedWordCloud.Utils import DEFAULT_ENG_FONT_PATH
from tests.TestDataGetter import timelapses_test


def test_calculate_font_size():
    # check max
    assert calculate_font_size(100, 100, 50, 50, 25) == 50
    assert calculate_font_size(1500, 1500, 50, 100, 25) == 100

    # check min
    assert calculate_font_size(50, 100, 50, 50, 25) == 25
    assert calculate_font_size(50, 1500, 50, 100, 25) == 25

    # check monotone increasing
    assert calculate_font_size(6.3, 10.0, 0.0, 1000, 5) >= calculate_font_size(
        3.0, 10.0, 0.0, 1000, 5
    )
    assert calculate_font_size(6.3, 10.0, 0.0, 1000, 5) >= calculate_font_size(
        6.0, 10.0, 0.0, 1000, 5
    )


def test_estimate_text_size():
    # just a exceessive test
    assert estimate_text_size("Hello", 100, DEFAULT_ENG_FONT_PATH)[0] > 50
    assert estimate_text_size("Hello", 100, DEFAULT_ENG_FONT_PATH)[1] > 50


def test_allocate():
    # TODO: make after Random Allocater made
    pass
