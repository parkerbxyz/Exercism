from math import sqrt
from typing import Union

Point = Union[int, float]


def score(x: Point, y: Point) -> int:
    """Returns the earned points in a single toss of a Darts game."""
    distance = sqrt(x**2 + y**2)
    if distance <= 1:  # inner circle of the target
        return 10
    elif distance <= 5:  # middle circle of the target
        return 5
    elif distance <= 10:  # outer circle of the target
        return 1
    else:
        return 0  # outside the target
