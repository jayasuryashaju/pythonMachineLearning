"""
module have two functions.
1. days_between(date_from, date_to)
    this takes two arguments those are date objects and returns the number of days between the dates

2. add_days(date, days)
    this takes a date and a number of days as arguments and returns a date with the days added to the date given
"""
from datetime import datetime, timedelta


def days_between(date_from=None, date_to=None):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(date_from, date_format)
    end_date = datetime.strptime(date_to, date_format)
    delta = end_date - start_date
    return delta.days


def add_days(date, days):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(date, date_format)
    end_date = start_date + timedelta(days=days)
    return end_date.strftime(date_format)


