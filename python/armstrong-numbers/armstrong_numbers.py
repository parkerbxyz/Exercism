from typing import List


def is_armstrong(number: int) -> bool:
    """Return True if the given number is an armstrong number."""
    digits = list(map(int, str(number)))
    exponent = len(digits)
    powers: List[int] = [base ** exponent for base in digits]
    return sum(powers) == number
