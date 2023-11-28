# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Testing the Word module
"""

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationCalculator.StaticAllocationStrategies.Word import (
    Word,
)


def test_word():
    instance = Word("test", 10, 20, (0, 0))
    assert instance.text == "test"
    assert instance.weight == 10
    assert instance.font_size == 20
    assert instance.text_size == (0, 0)
