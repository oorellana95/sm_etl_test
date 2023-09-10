import pytest

from etl.services.general_functions.validation import (
    contains_list_of_emails,
    is_valid_email,
)


def test_valid_email():
    """Test if valid email addresses are correctly identified."""
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("user123@gmail.com") is True


def test_invalid_email():
    """Test if an invalid email address raises a ValueError."""
    with pytest.raises(
        ValueError, match=r"Incorrect data format, should be a valid email"
    ):
        is_valid_email("invalid-email")


def test_missing_at_symbol():
    """Test if an email without the '@' symbol raises a ValueError."""
    with pytest.raises(
        ValueError, match=r"Incorrect data format, should be a valid email"
    ):
        is_valid_email("example.com")


def test_missing_dot_after_domain():
    """Test if an email without a dot after the domain raises a ValueError."""
    with pytest.raises(
        ValueError, match=r"Incorrect data format, should be a valid email"
    ):
        is_valid_email("test@example")


def test_email_with_special_characters():
    """Test if an email with special characters is correctly identified."""
    assert is_valid_email("user.name+tag@example-domain.co.uk") is True


def test_contains_valid_emails():
    """Test if a list containing valid email addresses is correctly identified."""
    assert contains_list_of_emails(["test@example.com", "user123@gmail.com"]) is True


def test_contains_invalid_email():
    """Test if a list containing an invalid email address raises a ValueError."""
    with pytest.raises(
        ValueError, match=r"Incorrect data format, should be a valid email"
    ):
        contains_list_of_emails(["test@example.com", "invalid-email"])
