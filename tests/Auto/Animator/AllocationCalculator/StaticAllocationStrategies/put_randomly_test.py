# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
testing put_randomly()
"""

from AnimatedWordCloud.Animator.AllocationCalculator.StaticAllocationStrategies.put_randomly import (
    put_randomly,
)


def test_put_randomly():
    assert put_randomly(100, 100, (10, 10)) is not None
