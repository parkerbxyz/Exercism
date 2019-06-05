def is_isogram(string: str) -> bool:
    """Return True if a given word or phrase is an isogram."""
    letters = [letter for letter in string.casefold() if letter.isalpha()]
    return len(letters) == len(set(letters))
