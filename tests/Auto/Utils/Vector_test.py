# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Testing the Vector classes
"""

from AnimatedWordCloud.Utils import Vector
from pytest import raises


def test_vector():
    vec1 = Vector(1, 2)
    vec2 = Vector((3, 4))

    # plus
    plus = vec1 + vec2
    assert plus.x == 4
    assert plus.y == 6

    # minus
    minus = vec1 - vec2
    assert minus.x == -2
    assert minus.y == -2

    # multiply
    multiply = vec1 * 2
    assert multiply.x == 2
    assert multiply.y == 4

    # divide
    divide = vec1 / 2
    assert divide.x == 0.5
    assert divide.y == 1

    # get item
    assert vec1[0] == 1
    assert vec1[1] == 2

    # clone
    clone = vec1.clone()
    clone += vec2
    assert clone.x == 4
    assert clone.y == 6
    assert vec1.x == 1
    assert vec1.y == 2

    # convert to tuple
    tup = vec1.convert_to_tuple()
    assert tup == (1, 2)

    # convert to str
    assert str(vec1) is str

    # invalid constructing
    with raises(ValueError):
        Vector(1, 2, 3)

    with raises(ValueError):
        Vector((1, 2, 3))
