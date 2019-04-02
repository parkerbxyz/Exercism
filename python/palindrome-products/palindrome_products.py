"""Detect palindrome products in a given range."""


def largest_palindrome(max_factor: int, min_factor: int = 0) -> tuple:
    """Return the largest palindrome and its factors within a given range."""
    extreme_range = range(max_factor ** 2, min_factor ** 2 - 1, -1)
    return _palindrome(min_factor, max_factor, extreme_range)


def smallest_palindrome(max_factor: int, min_factor: int = 0) -> tuple:
    """Return the smallest palindrome and its factors within a given range."""
    extreme_range = range(min_factor ** 2, max_factor ** 2 + 1)
    return _palindrome(min_factor, max_factor, extreme_range)


def _palindrome(minimum: int, maximum: int, extreme_range: range) -> tuple:
    if minimum > maximum:
        raise ValueError("Max factor must be greater than min factor.")

    def is_palindrome(number: int) -> bool:
        return str(number) == str(number)[::-1]

    inclusive_range = range(minimum, maximum + 1)

    def factor_pairs(number: int):
        return ((i, number // i) for i in inclusive_range
                if number % i == 0 and number // i in inclusive_range)

    for i in extreme_range:
        if (is_palindrome(i)
                and any(i//j in inclusive_range
                        for j in inclusive_range if i % j == 0)):
            return (i, factor_pairs(i))

    return (None, [])  # if there are no palindromes within the given range
