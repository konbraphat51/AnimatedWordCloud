# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Heart of animation flow
Get the input and returns the output, 
    calling each modules
"""

from typing import Dict, Tuple
from collections.abc import Iterable


def animate(word_vector_timelapse: Iterable[Tuple[str, Dict[str, float]]]) -> str:
    """
    Create an animation of word cloud,
        from the timelapse data of words vectors

    This function will call each modules in the right order,
        and return the animation path

    :param Iterable[Tuple[str, Dict[str, float]]] word_vector_timelapse:
    Timelapse data of word vectors.
    The data structure is a list of tuples,
        which includes "name of the time(str)" and "word vector(Dict[str, float])"
    :return: The path of the animation file.
    :rtype: str
    """

    return ""
