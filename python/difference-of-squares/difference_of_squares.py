def square_of_sum(count: int) -> int:
    numbers = range(count + 1)
    return sum(numbers) ** 2


def sum_of_squares(count: int) -> int:
    numbers = range(count + 1)
    squares = (x ** 2 for x in numbers)
    return sum(squares)


def difference(count: int) -> int:
    return square_of_sum(count) - sum_of_squares(count)
