from typing import Dict

LETTER_VALUES = (
    ('A, E, I, O, U, L, N, R, S, T',    1),
    ('D, G',                            2),
    ('B, C, M, P',                      3),
    ('F, H, V, W, Y',                   4),
    ('K',                               5),
    ('J, X',                            8),
    ('Q, Z',                            10)
)

POINTS: Dict[str, int] = {
    letter: value for letters, value in LETTER_VALUES
    for letter in letters.split(', ')
}


def score(word: str) -> int:
    """Return the Scrabble score for the word."""
    word = word.upper()
    return sum(POINTS.get(letter, 0) for letter in word)
