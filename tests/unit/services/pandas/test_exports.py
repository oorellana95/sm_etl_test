import os
from datetime import datetime

import pandas as pd
from etl.services.pandas.exports import (
    handle_dataframe_missing_mandatory_values,
    save_dataframe_to_timestamped_csv,
)

# Define a sample DataFrame for testing
data = pd.DataFrame(
    {
        "A": [1, 2, None, 4, 5],
        "B": [None, 2, 3, 4, None],
    }
)


def test_save_dataframe_to_timestamped_csv(temp_dir):
    """Test if the function correctly saves a DataFrame to a timestamped CSV file."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename_prefix = "test_data"
    expected_filename = f"{timestamp}_{filename_prefix}.csv"
    expected_file_path = os.path.join(temp_dir, expected_filename)

    file_path = save_dataframe_to_timestamped_csv(data, filename_prefix)

    assert os.path.exists(file_path)
    assert file_path == expected_file_path


def test_handle_dataframe_missing_mandatory_values(temp_dir):
    """Test if the function correctly handles a DataFrame with missing mandatory values."""
    prefix_filename = "test"
    file_path = handle_dataframe_missing_mandatory_values(data, prefix_filename)

    assert os.path.exists(file_path)
