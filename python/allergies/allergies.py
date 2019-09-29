from enum import IntFlag, auto
from typing import List


class Allergens(IntFlag):
    """Allergens and their values, which are powers of two (1, 2, 4, 8, …)."""
    EGGS = auto()
    PEANUTS = auto()
    SHELLFISH = auto()
    STRAWBERRIES = auto()
    TOMATOES = auto()
    CHOCOLATE = auto()
    POLLEN = auto()
    CATS = auto()


class Allergies:
    def __init__(self, score: int):
        self.flags = Allergens(score)

    def allergic_to(self, item: str) -> bool:
        """Return True if allergic to the given item; otherwise False."""
        return Allergens[item.upper()] in self.flags

    @property
    def lst(self) -> List[str]:
        """Return the full list of allergies."""
        return [allergen.name.lower() for allergen in Allergens
                if allergen in self.flags]
