"""
Validation functions - Pandas module
The functions are all meant to check specific type of data or lengths considering pandas objects as parameters.
"""
import pandas as pd


def check_array_str_lengths(
    data: pd.DataFrame, column_arrays_name: str, column_control_numbers_name: str
):
    # Define a function to check if array length matches the specified length
    def is_length_match(row):
        array_length = len(eval(row[column_arrays_name]))
        specified_length = row[column_control_numbers_name]
        return array_length == specified_length

    # Apply the length matching function to each row in the DataFrame
    length_match_series = data.apply(is_length_match, axis=1)

    # If any length mismatches are found, raise an IndexError
    if not length_match_series.all():
        raise IndexError(
            f"Array length mismatches with its control_number {column_arrays_name}, {column_control_numbers_name}"
        )
