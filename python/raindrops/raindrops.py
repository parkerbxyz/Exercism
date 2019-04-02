from typing import Dict, List

RAINDROP_FACTORS: Dict[int, str] = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong'
}


def raindrops(number: int) -> str:
    """Convert a number to raindrop-speak."""
    raindrop_factors = _get_raindrop_factors(number)
    drops = [RAINDROP_FACTORS.get(factor) for factor in raindrop_factors]
    return ''.join(map(str, drops)) or str(number)


def _get_factors(number: int) -> List[int]:
    """Return all factors of a given integer."""
    return [i for i in range(1, number + 1) if number % i == 0]


def _get_raindrop_factors(number: int) -> List[int]:
    """Return all raindrop factors of a given integer."""
    return [i for i in _get_factors(number) if i in RAINDROP_FACTORS]
