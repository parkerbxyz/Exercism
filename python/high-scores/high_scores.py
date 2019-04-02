from heapq import nlargest
from typing import List

from dataclasses import dataclass


@dataclass
class HighScores:
    scores: List[int]

    def latest(self):
        """The last added score."""
        return self.scores[-1]

    def personal_best(self):
        """The highest score."""
        return max(self.scores)

    def personal_top(self):
        """The three highest scores."""
        return nlargest(3, self.scores)

    def report(self):
        """The difference between the last and the highest scores."""
        difference = self.personal_best() - self.latest()
        result_qualifier = (f"{difference} short of " if difference else "")
        return (f"Your latest score was {self.latest()}. " +
                f"That's {result_qualifier}your personal best!")
