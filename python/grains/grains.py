from functools import wraps


def validate_range(func):
    @wraps(func)
    def wrapper(number: int) -> int:
        if number > 64 or number < 1:
            raise ValueError("Invalid input. Must be in the range 1-64.")
        return func(number)
    return wrapper


@validate_range
def on_square(number: int) -> int:
    return (2 ** number - 1) - (2 ** (number - 1) - 1)


@validate_range
def total_after(number: int) -> int:
    return 2 ** number - 1
