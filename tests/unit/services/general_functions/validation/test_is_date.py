import pytest
from etl.services.general_functions.validation import is_date, contains_all_dates


def test_valid_date():
    """Valid input: A date string in the correct format."""
    assert is_date("2023-09-09") is True


def test_valid_date_alternate_format():
    """Invalid input: A date string in a different format."""
    with pytest.raises(ValueError, match="Incorrect data format, should be YYYY-MM-DD"):
        is_date("05/20/2022")


def test_not_a_date():
    """Invalid input: A string that is not a date."""
    with pytest.raises(ValueError, match="Incorrect data format, should be YYYY-MM-DD"):
        is_date("Not a date")


def test_leap_year_date():
    """Valid input: A leap year date."""
    assert is_date("2024-02-29") is True


def test_invalid_leap_year_date():
    """Invalid input: A leap year date in a non-leap year."""
    with pytest.raises(ValueError, match="Incorrect data format, should be YYYY-MM-DD"):
        is_date("2023-02-29")


def test_valid_date_with_extra_characters():
    """Invalid input: A valid date with extra characters."""
    with pytest.raises(ValueError, match="Incorrect data format, should be YYYY-MM-DD"):
        is_date("2023-09-09extra")


def test_empty_string():
    """Invalid input: An empty string."""
    with pytest.raises(ValueError, match="Incorrect data format, should be YYYY-MM-DD"):
        is_date("")


def test_contains_invalid_dates():
    """Check if contains_all_dates correctly validates a list of dates."""
    invalid_date_list = ["2023-09-09", "2022-05-20", "20-05-2022"]

    with pytest.raises(ValueError, match="Incorrect data format, should be YYYY-MM-DD"):
        contains_all_dates(invalid_date_list)