import pytest

from etl.services.general_functions.validation import contains_all_valid_ranking_numbers


def test_valid_ranking_numbers():
    """Check if contains_all_valid_ranking_numbers correctly validates a list of valid ranking numbers."""
    valid_ranking_list = [0, 1, 2, 3, 4, 5]
    result = contains_all_valid_ranking_numbers(valid_ranking_list)
    assert result is True


def test_invalid_ranking_numbers():
    """Check if contains_all_valid_ranking_numbers correctly raises a ValueError for invalid ranking numbers."""
    invalid_ranking_list = [-1, 0, 1, 2, 6, 7]

    with pytest.raises(ValueError, match="Incorrect value, should be between 0 and 5"):
        contains_all_valid_ranking_numbers(invalid_ranking_list)


def test_mixed_ranking_numbers():
    """Check if contains_all_valid_ranking_numbers correctly raises a ValueError for a mix of valid and invalid
    ranking numbers."""
    mixed_ranking_list = [0, 1, 2, 3, 4, 5, 6, 7]

    with pytest.raises(ValueError, match="Incorrect value, should be between 0 and 5"):
        contains_all_valid_ranking_numbers(mixed_ranking_list)
