from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    """Returns the correct sublist of a word and list of possible anagrams."""
    return [c for c in candidates if is_anagram(word, c)]


def is_anagram(w1: str, w2: str) -> bool:
    w1, w2 = w1.casefold(), w2.casefold()
    return w2 != w1 and sorted(w2) == sorted(w1)
