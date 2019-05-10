from functools import wraps
from typing import Callable


def validate_range(func: Callable[[int], int]) -> Callable[[int], int]:
    """Raise an exception if a given number is outside of the valid range."""
    @wraps(func)
    def wrapper(number: int) -> int:
        if number > 64 or number < 1:  # There are 64 squares on a chessboard.
            raise ValueError("Invalid input. Must be in the range 1-64.")
        return func(number)
    return wrapper


@validate_range
def on_square(number: int) -> int:
    """Return the number of grains on a given square."""
    return 1 << (number - 1)


@validate_range
def total_after(number: int) -> int:
    """Return the total number of grains up to a given square."""
    return (1 << number) - 1
