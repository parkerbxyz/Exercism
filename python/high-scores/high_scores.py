from heapq import nlargest
from typing import List

Scores = List[int]


def latest(scores: Scores) -> int:
    """The last added score."""
    return scores[-1]


def personal_best(scores: Scores) -> int:
    """The highest score."""
    return max(scores)


def personal_top_three(scores: Scores) -> Scores:
    """The three highest scores."""
    return nlargest(3, scores)
