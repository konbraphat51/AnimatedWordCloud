# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Testing the Vector classes
"""

from AnimatedWordCloud.Utils import Vector

def test_vector():
    vec1 = Vector(1, 2)
    vec2 = Vector((3, 4))
    
    #plus
    plus = vec1 + vec2
    assert plus.x == 4
    assert plus.y == 6
    
    #minus
    minus = vec1 - vec2
    assert minus.x == -2
    assert minus.y == -2
    
    #clone
    clone = vec1.clone()
    clone += vec2
    assert clone.x == 4
    assert clone.y == 6
    assert vec1.x == 1
    assert vec1.y == 2
    
    #convert to tuple
    tup = vec1.convert_to_tuple()
    assert tup == (1, 2)