from collections import Counter
from typing import List

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def get_set_value(dice: List[int], set_size: int) -> int:
    """Return the value of a set of dice."""
    set_value = 0
    for value, count in Counter(dice).items():
        if count == set_size:
            set_value = value
    return set_value


def score(dice: List[int], category: int) -> int:
    """Return the score of the dice for a given category."""
    points: int
    twos = get_set_value(dice, TWOS)
    threes = get_set_value(dice, THREES)
    fours = get_set_value(dice, FOURS)
    fives = get_set_value(dice, FIVES)

    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        points = category * dice.count(category)

    elif category is FULL_HOUSE:
        points = sum(dice) if twos and threes else 0

    elif category is FOUR_OF_A_KIND:
        points = max(fours, fives) * 4

    elif category is LITTLE_STRAIGHT:
        points = 30 if set(dice) == {1, 2, 3, 4, 5} else 0

    elif category is BIG_STRAIGHT:
        points = 30 if set(dice) == {2, 3, 4, 5, 6} else 0

    elif category is CHOICE:
        points = sum(dice)

    elif category is YACHT:
        points = 50 if fives else 0

    return points
