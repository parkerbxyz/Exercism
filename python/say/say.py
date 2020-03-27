ONES = ['zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

TENS = ['zero', 'ten', 'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def say(number: int) -> str:
    """Spells out a given number from 0 to 999,999,999,999 in English."""
    if number not in range(int(1e12)):
        raise ValueError("Number must be between 0 and 999,999,999,999!")
    if number < 20:
        return ONES[number]
    elif number < 100:
        ten, remainder = divmod(number, 10)
        return TENS[ten] + (
            f"-{say(remainder)}" if remainder else '')
    elif number < 1000:
        hundred, remainder = divmod(number, 100)
        return ONES[hundred] + ' hundred' + (
            f" {say(remainder)}" if remainder else '')
    elif number < 1000000:
        thousand, remainder = divmod(number, 1000)
        return say(thousand) + ' thousand' + (
            f" {say(remainder)}" if remainder else '')
    elif number < 1000000000:
        million, remainder = divmod(number, 1000000)
        return say(million) + ' million' + (
            f" {say(remainder)}" if remainder else '')
    else:
        billion, remainder = divmod(number, 1000000000)
        return say(billion) + ' billion' + (
            f" {say(remainder)}" if remainder else '')
