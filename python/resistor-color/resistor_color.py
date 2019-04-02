from typing import Dict, List

COLOR_CODE: Dict[str, int] = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey':  8,
    'white': 9
}


def color_code(color: str) -> int:
    """Return the significant digit of a given color."""
    return COLOR_CODE[color]


def colors() -> List[str]:
    """Return the colors with corresponding significant digits."""
    return list(COLOR_CODE.keys())
