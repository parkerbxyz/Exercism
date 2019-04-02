"""Determine if a triangle is equilateral, isosceles, or scalene."""

from typing import List


def is_triangle(sides: List[int]) -> bool:
    """Return True if the given side lengths form a triangle."""
    return (len(sides) == 3  # has three side lengths
            and all(s > 0 for s in sides)  # all side lengths are positive
            and max(sides) <= sum(sides) - max(sides))  # degenerate inclusive


def is_equilateral(sides: List[int]) -> bool:
    """Return True the triangle is equilateral."""
    # an equilateral triangle has all three sides the same length
    return is_triangle(sides) and len(set(sides)) == 1


def is_isosceles(sides: List[int]) -> bool:
    """Return True if the triangle is isosceles"""
    # an isosceles triangle has at least two sides the same length
    return is_triangle(sides) and len(set(sides)) <= 2


def is_scalene(sides: List[int]) -> bool:
    """Return True if the triangle is scalene."""
    # a scalene triangle has all sides of different lengths
    return is_triangle(sides) and len(set(sides)) == 3


def is_degenerate(sides: List[int]) -> bool:
    """Return True if the sum of the lengths of two sides equals the third."""
    # a degenerate triangle has zero area and looks like a single line
    return is_triangle(sides) and max(sides) == sum(sides) - max(sides)
