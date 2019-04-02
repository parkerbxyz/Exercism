import operator
import re

PATTERN = re.compile(r"""^\d-?    # first digit followed by a hyphen 0-1 times
                         \d{3}-?  # 3 digits followed by a hyphen 0-1 times
                         \d{5}-?  # 5 digits followed by a hyphen 0-1 times
                         [\d|X]$  # final (check) digit (X is used for 10)
                         """, re.X)


def verify(isbn: str) -> bool:
    """Checks if the provided string is a valid ISBN-10."""
    if not PATTERN.match(isbn):
        return False
    isbn = isbn.replace('-', '')
    vector1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    vector2 = [10 if d == 'X' else int(d) for d in isbn]
    dot_product = sum(map(operator.mul, vector1, vector2))
    return dot_product % 11 == 0
