"""Output the lyrics to 'The Twelve Days of Christmas' song."""

from typing import List


DAYS = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

GIFTS = ['a Partridge in a Pear Tree',
         'two Turtle Doves',
         'three French Hens',
         'four Calling Birds',
         'five Gold Rings',
         'six Geese-a-Laying',
         'seven Swans-a-Swimming',
         'eight Maids-a-Milking',
         'nine Ladies Dancing',
         'ten Lords-a-Leaping',
         'eleven Pipers Piping',
         'twelve Drummers Drumming']


def verse(number: int) -> str:
    """Return a single verse from 'The Twelve Days of Christmas' song."""
    gifts = GIFTS[number - 1:: -1]
    if number > 1:
        gifts[-1] = 'and ' + gifts[-1]
    return f"On the {DAYS[number]} day of Christmas my true love gave to me: "\
           f"{', '.join(gifts)}."


def recite(start_verse: int, end_verse: int) -> List[str]:
    """Return a range of verses from 'The Twelve Days of Christmas' song."""
    return [verse(number) for number in range(start_verse, end_verse + 1)]
