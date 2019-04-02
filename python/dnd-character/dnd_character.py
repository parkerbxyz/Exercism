from heapq import nlargest
from math import floor
from random import randint


def roll_d6(number):
    results = []
    for _ in range(number):
        results.append(randint(1, 6))
    return results


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

    @staticmethod
    def ability():
        return sum(nlargest(3, roll_d6(4)))

    @property
    def hitpoints(self):
        return 10 + modifier(self.constitution)


def modifier(value):
    return floor((value - 10) / 2)
