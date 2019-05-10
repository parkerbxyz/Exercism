def hey(phrase: str) -> str:
    """Return Bob's response to a given phrase."""
    phrase = phrase.strip()
    if phrase.endswith('?'):
        return ("Calm down, I know what I'm doing!"
                if phrase.isupper() else "Sure.")
    if phrase.isupper():
        return "Whoa, chill out!"
    if not phrase:
        return "Fine. Be that way!"
    return "Whatever."
