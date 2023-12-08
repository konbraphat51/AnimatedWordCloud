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

    def __init__(self, **args: float | tuple[float, float]) -> None:
        """
        Initialize Vector class.

        :param args: x and y or tuple of x and y
        input as Vector(x, y) or Vector((x, y))
        """
        if args[0].__class__ == tuple:
            self.x = args[0][0]
            self.y = args[0][1]
        elif len(args) == 2:
            # x_or_tuple is float
            self.x = args[0]
            self.y = args[1]

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

    def __mul__(self, other: float) -> Vector:
        """
        Product of vector and scalar.

        :return: product of vector and scalar
        :rtype: Vector
        """
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> Vector:
        """
        Division of vector and scalar.

        :return: division of vector and scalar
        :rtype: Vector
        """
        return Vector(self.x / other, self.y / other)

    def __getitem__(self, index: int) -> float:
        """
        Get item by index.

        :return: x if index is 0, y if index is 1
        :rtype: float
        """
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError(f"Index {index} is out of range")

    def __str__(self) -> str:
        """
        Convert to string.

        :return: string representation of the vector
        :rtype: str
        """
        return f"({self.x}, {self.y})"

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
