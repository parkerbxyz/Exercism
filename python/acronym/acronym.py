import re
from typing import List, Pattern


def abbreviate(phrase: str) -> str:
    """Convert a phrase to its acronym."""
    words: Pattern[str] = re.compile(r"[A-Za-z']+")
    word_list: List[str] = words.findall(phrase)
    acronym = ''.join(word[0] for word in word_list).upper()
    return acronym
