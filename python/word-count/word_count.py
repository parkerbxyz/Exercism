import re
from typing import Counter, List, Pattern


WORDS: Pattern[str] = re.compile(r"""
    [a-z]+ (?:'[a-z]+)?  # words (including contractions)
    | [0-9]+             # or numbers
    """, re.X)


def word_count(phrase: str) -> Counter[str]:
    """Counts the occurrences of each word in a given phrase."""
    word_list: List[str] = re.findall(WORDS, phrase.casefold())
    return Counter(word_list)
