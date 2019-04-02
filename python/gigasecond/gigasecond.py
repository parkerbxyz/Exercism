from datetime import datetime, timedelta

GIGASECOND = timedelta(seconds=10**9)  # 1,000,000,000 seconds


def add_gigasecond(moment: datetime) -> datetime:
    """Add one gigasecond to a given date and time."""
    return moment + GIGASECOND
