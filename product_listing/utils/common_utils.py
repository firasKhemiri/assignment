"""This module contains functions are necessary for other functions to work."""
from datetime import datetime

from product_listing.exceptions import InvalidDate


def calculate_passed_time(first_date: datetime, second_date: datetime) -> str:
    """Calculate the elapsed time between two dates."""
    if first_date.replace(tzinfo=None) < second_date.replace(tzinfo=None):
        raise InvalidDate

    period = first_date.replace(tzinfo=None) - second_date.replace(tzinfo=None)
    if period.days > 0:
        result = f"{period.days} days ago"
    else:
        result = _convert_seconds(period.seconds)

    return result


def _convert_seconds(seconds: int) -> str:
    """Extract how many hours, minutes and seconds in a certain amount of seconds"""
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    if hour > 0:
        return f"{hour} hours ago"
    if minutes > 0:
        return f"{minutes} minutes ago"

    return f"{seconds} seconds ago"
