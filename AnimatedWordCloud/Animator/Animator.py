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

from __future__ import annotations
from typing import Iterable


def animate(
    word_vector_timelapse: Iterable[tuple[str, dict[str, float]]]
) -> str:
    """
    Create an animation of word cloud,
        from the timelapse data of words vectors

    This function will call each modules in the right order,
        and return the animation path

    :param Iterable[tuple[str, dict[str, float]]] word_vector_timelapse:
    Timelapse data of word vectors.
    The data structure is a list of tuples,
        which includes "name of the time(str)" and "word vector(Dict[str, float])"
    :return: The path of the animation file.
    :rtype: str
    """

    return ""
