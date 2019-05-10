def is_isogram(string: str) -> bool:
    letters = [letter.casefold() for letter in string if letter.isalpha()]
    return len(letters) == len(set(letters))
