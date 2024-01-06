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

    def __init__(self, *args: float | tuple[float, float]) -> None:
        """
        Initialize Vector class.

        :param args: x and y or tuple of x and y
        input as Vector(x, y) or Vector((x, y))
        """

        # if the input is tuple...
        if args[0].__class__ == tuple:
            # ...ensuring (float, float)
            if len(args[0]) != 2:
                raise ValueError("Tuple must have 2 elements")

            # if the value was not a number, this intends to raise an error
            self.x = float(args[0][0])
            self.y = float(args[0][1])
        elif len(args) == 2:
            # ...x, y are seperatedly input

            # if the value was not a number, this intends to raise an error
            self.x = float(args[0])
            self.y = float(args[1])
        else:
            raise ValueError("Invalid Vector input")

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

    def cross(vec0: Vector, vec1: Vector) -> float:
        """
        Cross product of two vectors.
        This is static method.

        :param Vector vec0: Vector 0
        :param Vector vec1: Vector 1
        :return: Cross product of two vectors
        :rtype: float
        """
        return vec0.x * vec1.y - vec0.y * vec1.x
