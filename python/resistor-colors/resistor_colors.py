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


def value(colors: List[str]) -> int:
    values = [COLOR_CODE.get(color) for color in colors]
    return int("".join(map(str, values)))
