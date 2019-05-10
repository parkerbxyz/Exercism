from math import sqrt
from typing import Union

Point = Union[int, float]


def score(x: Point, y: Point) -> int:
    """Returns the earned points in a single toss of a Darts game."""
    distance = sqrt(x**2 + y**2)
    if distance > 10:  # outside the target
        return 0
    if distance > 5:  # outer circle of the target
        return 1
    if distance > 1:  # middle circle of the target
        return 5
    return 10  # inner circle of the target
