# -*- coding: utf-8 -*-
# Copyright (C) 2023 AnimatedWordCloud Project
# https://github.com/konbraphat51/AnimatedWordCloud
#
# Licensed under the MIT License.
"""
Modules for 2D vector calculation
"""

from __future__ import annotations


class Vector:
    """
    Class for 2D vector calculation
    """

    def __init__(
        self, x_or_tuple: float | tuple[float, float], y: float = 0
    ) -> None:
        """
        Initialize Vector class.
        """
        if x_or_tuple.__class__ == tuple:
            self.x = x_or_tuple[0]
            self.y = x_or_tuple[1]
        else:
            # x_or_tuple is float
            self.x = x_or_tuple
            self.y = y

    def __add__(self, other: Vector) -> Vector:
        """
        Sum of two vectors.

        :return: sum of two vectors
        :rtype: Vector
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        """
        Difference of two vectors.

        :return: difference of two vectors
        :rtype: Vector
        """
        return Vector(self.x - other.x, self.y - other.y)

    def clone(self) -> Vector:
        """
        Clone this vector.

        So as modifying the output doesn't affect the original vector.

        :return: Cloned vector
        :rtype: Vector
        """
        return Vector(self.x, self.y)

    def convert_to_tuple(self) -> tuple[float, float]:
        """
        Convert to tuple

        :return: tuple of x and y
        :rtype: tuple[float, float]
        """
        return (self.x, self.y)
