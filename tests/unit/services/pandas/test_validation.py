import pytest

import pandas as pd
from etl.services.pandas.validation import check_array_str_lengths

# Create a sample DataFrame for testing
data = pd.DataFrame(
    {
        "arrays": ["['item1', 'item2', 'item3']", "['item4', 'item5']", "['item6']"],
        "control_numbers": [3, 2, 1],
    }
)


def test_check_array_str_lengths_valid():
    """Test if the function correctly handles valid array lengths."""
    check_array_str_lengths(data, "arrays", "control_numbers")


def test_check_array_str_lengths_invalid():
    """Test if the function raises an IndexError for invalid array lengths."""
    data_invalid = pd.DataFrame(
        {
            "arrays": [
                "['item1', 'item2', 'item3']",
                "['item4', 'item5']",
                "['item6', 'item7']",
            ],
            "control_numbers": [3, 2, 1],
        }
    )

    with pytest.raises(
        IndexError,
        match=r"Array length mismatches with its control_number arrays, control_numbers",
    ):
        check_array_str_lengths(data_invalid, "arrays", "control_numbers")
