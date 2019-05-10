def is_isogram(string: str) -> bool:
    """Return True if a given word or phrase is an isogram."""
    letters = [letter.casefold() for letter in string if letter.isalpha()]
    return len(letters) == len(set(letters))
