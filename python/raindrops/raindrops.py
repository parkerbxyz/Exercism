from enum import IntEnum


class Drops(IntEnum):
    Pling = 3
    Plang = 5
    Plong = 7


def raindrops(number: int) -> str:
    """Convert a number to raindrop-speak."""
    drops = [drop.name for drop in Drops if not number % drop.value]
    return ''.join(drops) or str(number)
