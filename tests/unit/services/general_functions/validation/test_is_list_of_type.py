import pytest

from etl.services.general_functions.validation import contains_list_of_floats, is_list_of_type, contains_list_of_strings


def test_valid_list_of_integers():
    """Test if a valid list of integers is correctly identified."""
    assert is_list_of_type("[1, 2, 3]", int) is True


def test_valid_list_of_floats():
    """Test if a valid list of floats is correctly identified."""
    assert is_list_of_type("[1.0, 2.5, 3.7]", float) is True


def test_valid_list_of_strings():
    """Test if a valid list of strings is correctly identified."""
    assert is_list_of_type("['apple', 'banana', 'cherry']", str) is True


def test_invalid_list_type():
    """Test if a list with an incorrect element type raises ValueError."""
    with pytest.raises(ValueError):
        is_list_of_type("[1, 'two', 3]", str)


def test_invalid_list_format():
    """Test if a list with a formatting error raises ValueError."""
    with pytest.raises(ValueError):
        is_list_of_type("[1, 2, 3", int)


def test_invalid_list_eval():
    """Test if a string that cannot be evaluated as a list raises ValueError."""
    with pytest.raises(ValueError):
        is_list_of_type("not_a_list", float)


def test_contains_valid_list_of_strings():
    """Check if contains_list_of_strings correctly validates a list of valid lists of strings."""
    valid_list_strings = ["['apple', 'banana']", "['cherry', 'date']", "['fig']"]
    result = contains_list_of_strings(valid_list_strings)
    assert result is True


def test_contains_list_of_strings():
    """Check if contains_list_of_strings correctly raises a ValueError for an invalid list of strings."""
    invalid_list_strings = ["['apple', 'banana']", 'cherry', "['fig']"]
    with pytest.raises(ValueError):
        contains_list_of_strings(invalid_list_strings)


def test_contains_valid_list_of_strings():
    """Check if contains_list_of_floats correctly validates a list of valid lists of floats."""
    valid_list_of_floats = ["[1.0, 2.5, 3.7]", "[1.0, 2.5, 3.7]"]
    result = contains_list_of_floats(valid_list_of_floats)
    assert result is True


def test_contains_list_of_floats():
    """Check if contains_list_of_floats correctly raises a ValueError for an invalid list of floats."""
    valid_list_floats = ["[1.0, 2.5, 3.7]", "[three]", "[1.0]"]
    with pytest.raises(ValueError):
        contains_list_of_floats(valid_list_floats)
