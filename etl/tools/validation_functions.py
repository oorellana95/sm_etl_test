"""
Validation functions:
The functions are all meant to check specific type of data. They can expect a list or just a single value.
"""
import datetime


def check_is_date(single_date_str: str):
    """Check if the value is a date. Format YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(single_date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def check_contains_all_date(list_dates_str: list):
    """Check if the list of values are dates. Format YYYY-MM-DD."""
    for value in list_dates_str:
        check_is_date(value)


def check_contains_all_valid_ranking_numbers(list_integers: list):
    """Check if the list of values are in between the ranking range 0-5."""
    min_ranking_value, max_ranking_value = 0, 5
    if (
        min(list_integers) < min_ranking_value
        or max(list_integers) > max_ranking_value
    ):
        raise ValueError(
            f"Incorrect value, should be between {min_ranking_value} and {max_ranking_value}"
        )


def check_is_list_of_strings(single_str_arr_str: list):
    try:
        parsed_list = eval(single_str_arr_str)
        if not isinstance(parsed_list, list) or not all(isinstance(item, str) for item in parsed_list):
            raise ValueError(f"The value '{single_str_arr_str}' is not a list of strings.")
    except (ValueError, SyntaxError):
        raise ValueError(f"Incorrect value, should be a list of strings: '{single_str_arr_str}'")


def check_contains_list_of_strings(list_strings: list):
    for value in list_strings:
        check_is_list_of_strings(value)


def check_is_list_of_floats(single_str_arr_float: list):
    try:
        parsed_list = eval(single_str_arr_float)
        if not isinstance(parsed_list, list) or not all(isinstance(item, float) for item in parsed_list):
            raise ValueError(f"The value '{single_str_arr_float}' is not a list of floats.")
    except (ValueError, SyntaxError):
        raise ValueError(f"Incorrect value, should be a list of floats: '{single_string}'")


def check_contains_list_of_floats(list_strings: list):
    for value in list_strings:
        check_is_list_of_floats(value)
