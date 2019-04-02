def is_armstrong(number):
    digits = list(map(int, str(number)))
    exponent = len(digits)
    powers = []
    for base in digits:
        powers.append(base ** exponent)
    return sum(powers) == number
