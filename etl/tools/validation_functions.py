"""
Validation functions:
The functions are all meant to check specific type of data. They can expect a list or just a single value.
"""
import datetime


def check_is_date(date_text: str):
    """Check if the value is a date. Format YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def check_contains_all_date(date_column: list):
    """Check if the list of values are dates. Format YYYY-MM-DD."""
    (check_is_date(value) for value in date_column)


def check_contains_all_valid_ranking_numbers(integer_column: list):
    """Check if the list of values are in between the ranking range 0-5."""
    min_ranking_value, max_ranking_value = 0, 4
    if (
        min(integer_column) < min_ranking_value
        or max(integer_column) > max_ranking_value
    ):
        raise ValueError(
            f"Incorrect value, should be between {min_ranking_value} and {max_ranking_value}"
        )