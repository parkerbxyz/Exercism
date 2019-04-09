def raindrops(number: int) -> str:
    """Convert a number to raindrop-speak."""
    drops = []
    if not number % 3:  # if the number has 3 as a factor
        drops.append('Pling')
    if not number % 5:  # if the number has 5 as a factor
        drops.append('Plang')
    if not number % 7:  # if the number has 7 as a factor
        drops.append('Plong')
    return ''.join(drops) or str(number)
