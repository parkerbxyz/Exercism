def is_pangram(sentence: str) -> bool:
    """Return True if given string is a panagram."""
    # a pangram is a sentence using every letter of the alphabet at least once
    sentence = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return set(sentence).issuperset(alphabet)
