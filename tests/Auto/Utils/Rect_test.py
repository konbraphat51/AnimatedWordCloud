# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Testing the Rect module
"""

from AnimatedWordCloud.Utils import Rect


def test_Rect():
    instance = Rect((0, 0), (100, 100))

    assert instance.left_top == (0, 0)
    assert instance.right_bottom == (100, 100)
