def hey(phrase: str) -> str:
    """Return Bob's response to a given phrase."""
    phrase = phrase.strip()
    if not phrase:  # if you address him without actually saying anything
        return "Fine. Be that way!"
    if phrase.isupper():  # if you yell at him
        if phrase.endswith('?'):   # if you yell a question at him
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if phrase.endswith('?'):  # if you ask him a question
        return "Sure."
    return "Whatever."  # to anything else
