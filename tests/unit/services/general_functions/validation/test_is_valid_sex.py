import pytest

from etl.services.general_functions.validation import (
    contains_list_of_sex_values,
    is_valid_sex,
)


def test_valid_sex_male():
    """Test if 'male' is recognized as a valid sex."""
    assert is_valid_sex("male") is True


def test_valid_sex_female():
    """Test if 'female' is recognized as a valid sex."""
    assert is_valid_sex("female") is True


def test_valid_sex_case_insensitive():
    """Test case-insensitivity when recognizing valid sexes."""
    assert is_valid_sex("Male") is True
    assert is_valid_sex("FeMaLe") is True


def test_invalid_sex():
    """Test if an invalid sex raises ValueError."""
    with pytest.raises(
        ValueError,
        match=r"Incorrect data format, should be a valid sex \(male or female\)",
    ):
        is_valid_sex("other")


def test_empty_string():
    """Test if an empty string raises ValueError."""
    with pytest.raises(
        ValueError,
        match=r"Incorrect data format, should be a valid sex \(male or female\)",
    ):
        is_valid_sex("")


def test_contains_valid_sex_values():
    """
    Test if the function correctly identifies a list containing valid sex values (male or female).
    """
    assert contains_list_of_sex_values(["male", "female", "male"]) is True


def test_contains_invalid_sex_value():
    """
    Test if the function raises the appropriate ValueError when it encounters an invalid sex value in the list.

    The function should raise a ValueError when the input list contains an invalid sex value.
    """
    with pytest.raises(
        ValueError,
        match=r"Incorrect data format, should be a valid sex \(male or female\)",
    ):
        contains_list_of_sex_values(["male", "other", "female"])
