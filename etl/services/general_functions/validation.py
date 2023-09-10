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
        return True
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def contains_all_dates(list_dates_str: list):
    """Check if the list of values are dates. Format YYYY-MM-DD."""
    for value in list_dates_str:
        is_date(value)
    return True


def contains_all_valid_ranking_numbers(list_integers: list):
    """Check if the list of values are in between the ranking range 0-5."""
    min_ranking_value, max_ranking_value = 0, 5
    if min(list_integers) < min_ranking_value or max(list_integers) > max_ranking_value:
        raise ValueError(
            f"Incorrect value, should be between {min_ranking_value} and {max_ranking_value}"
        )
    return True


def is_list_of_type(single_str_arr_type: str, type_to_check):
    """Check if the value is a list of the given type."""
    try:
        parsed_list = eval(single_str_arr_type)
        if not isinstance(parsed_list, list) or not all(
            isinstance(item, type_to_check) for item in parsed_list
        ):
            raise ValueError(
                f"The value '{single_str_arr_type}' is not a list of {type_to_check}."
            )
        return True
    except (ValueError, SyntaxError, NameError):
        raise ValueError(
            f"Incorrect value, should be a list of {type_to_check}: '{single_str_arr_type}'"
        )


def contains_list_of_strings(list_str_arr_str: list):
    """Check if the list of values are lists of strings. Input example: ['['apple', 'banana']', '['cherry', 'date']']"""
    for value in list_str_arr_str:
        is_list_of_type(single_str_arr_type=value, type_to_check=str)
    return True


def contains_list_of_floats(list_str_arr_float: list):
    """Check if the list of values are lists of floats. Input example: ['['3.3', '2.1']', '['0.3', '7.9']']"""
    for value in list_str_arr_float:
        is_list_of_type(single_str_arr_type=value, type_to_check=float)
    return True


def is_valid_email(email):
    """Check if the value is a valid email address."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    raise ValueError("Incorrect data format, should be a valid email")


def contains_list_of_emails(list_emails: list):
    """Check if the list of values are valid email addresses."""
    for email in list_emails:
        is_valid_email(email)
    return True


def is_valid_sex(sex):
    """Check if the value is a valid sex (male or female)."""
    if sex.lower() in ("male", "female"):
        return True
    raise ValueError("Incorrect data format, should be a valid sex (male or female)")


def contains_list_of_sex_values(sex_values: list):
    """Check if the list of values are valid sex values (male or female)."""
    for sex in sex_values:
        is_valid_sex(sex)
    return True
