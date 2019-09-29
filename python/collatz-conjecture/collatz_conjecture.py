def collatz_steps(number: int) -> int:
    """Return the number of steps required to prove the Collatz Conjecture."""
    if number <= 0 or not isinstance(number, int):
        raise ValueError("Number must be a positive, non-zero integer.")
    steps = 0
    while number != 1:
        number = number * 3 + 1 if number % 2 else number // 2
        steps += 1
    return steps
