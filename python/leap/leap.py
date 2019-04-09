def is_leap_year(year: int) -> bool:
    """Return True if a given year is a leap year."""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
