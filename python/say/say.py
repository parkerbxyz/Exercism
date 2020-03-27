ONES = ['zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

TENS = ['zero', 'ten', 'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def say(number):
    if number < 0 or number >= 1e12:
        raise ValueError("Number must be between 0 and 999,999,999,999!")
    if number < 20:
        return ONES[number]
    elif number < 100:
        ten = int(number / 10)
        remainder = number % 10
        return TENS[ten] + (
            f"-{say(remainder)}" if remainder else '')
    elif number < 1000:
        hundred = int(number / 100)
        remainder = number % 100
        return ONES[hundred] + ' hundred' + (
            f" and {say(remainder)}" if remainder else '')
    elif number < 1000000:
        thousand = int(number / 1000)
        remainder = number % 1000
        return say(thousand) + ' thousand' + (
            f" {say(remainder)}" if remainder else '')
    elif number < 1000000000:
        million = int(number / 1e6)
        remainder = int(number % 1e6)
        return say(million) + ' million' + (
            f" {say(remainder)}" if remainder else '')
    else:
        billion = int(number / 1e9)
        remainder = int(number % 1e9)
        return say(billion) + ' billion' + (
            f" {say(remainder)}" if remainder else '')
