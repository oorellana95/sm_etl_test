"""
Validation functions - General module
The functions are all meant to check specific type of data, lengths or compare.
"""
import datetime
import re


def is_date(single_date_str: str):
    """Check if the value is a date. Format YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(single_date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def contains_all_dates(list_dates_str: list):
    """Check if the list of values are dates. Format YYYY-MM-DD."""
    for value in list_dates_str:
        is_date(value)


def contains_all_valid_ranking_numbers(list_integers: list):
    """Check if the list of values are in between the ranking range 0-5."""
    min_ranking_value, max_ranking_value = 0, 5
    if min(list_integers) < min_ranking_value or max(list_integers) > max_ranking_value:
        raise ValueError(
            f"Incorrect value, should be between {min_ranking_value} and {max_ranking_value}"
        )


def is_list_of_strings(single_str_arr_str: list):
    """Check if the value is a list of strings."""
    try:
        parsed_list = eval(single_str_arr_str)
        if not isinstance(parsed_list, list) or not all(
            isinstance(item, str) for item in parsed_list
        ):
            raise ValueError(
                f"The value '{single_str_arr_str}' is not a list of strings."
            )
    except (ValueError, SyntaxError):
        raise ValueError(
            f"Incorrect value, should be a list of strings: '{single_str_arr_str}'"
        )


def contains_list_of_strings(list_strings: list):
    """Check if the list of values are lists of strings."""
    for value in list_strings:
        is_list_of_strings(value)


def is_list_of_floats(single_str_arr_float: list):
    """Check if the value is a list of floats."""
    try:
        parsed_list = eval(single_str_arr_float)
        if not isinstance(parsed_list, list) or not all(
            isinstance(item, float) for item in parsed_list
        ):
            raise ValueError(
                f"The value '{single_str_arr_float}' is not a list of floats."
            )
    except (ValueError, SyntaxError):
        raise ValueError(
            f"Incorrect value, should be a list of floats: '{single_str_arr_float}'"
        )


def contains_list_of_floats(list_strings: list):
    """Check if the list of values are lists of floats."""
    for value in list_strings:
        is_list_of_floats(value)


def is_valid_email(email):
    """Check if the value is a valid email address."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return
    raise ValueError("Incorrect data format, should be a valid email")


def contains_list_of_emails(list_emails: list):
    """Check if the list of values are valid email addresses."""
    for email in list_emails:
        is_valid_email(email)


def is_valid_sex(sex):
    """Check if the value is a valid sex (male or female)."""
    if sex.lower() in ("male", "female"):
        return
    raise ValueError("Incorrect data format, should be a valid sex (male or female)")


def contains_list_of_sex_values(sex_values: list):
    """Check if the list of values are valid sex values (male or female)."""
    for sex in sex_values:
        is_valid_sex(sex)
