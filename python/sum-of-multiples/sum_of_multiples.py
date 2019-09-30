from typing import List


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    """Return the sum of all unique multiples of n less than
    the 'limit' value for every n in the 'multiples' value.
    """
    unique_multiples: set = set()
    for multiple in (multiple for multiple in multiples if multiple != 0):
        for number in range(multiple, limit, multiple):
            unique_multiples.add(number)
    return sum(unique_multiples)
