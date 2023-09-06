"""
ProcessFileRecipes Class
Custom class inherited from the ProcessFile Class with the Interactions specifications to process the file.
"""

from etl.config import RAW_RECIPES_PATH
from etl.exceptions.file_processing_validation_exception import (
    ArrayLengthMismatchControlNumberError,
)
from etl.process_file.column_checker import ColumnChecker
from etl.process_file.file_data_processor import FileDataProcessor
from etl.tools.validation_functions.general_functions import (
    contains_all_dates,
    contains_list_of_floats,
    contains_list_of_strings,
)
from etl.tools.validation_functions.pandas_functions import check_array_str_lengths


class FileDataProcessorRecipes(FileDataProcessor):
    def __init__(self):
        super().__init__()
        self.file_type = "csv"
        self.file_path = RAW_RECIPES_PATH
        self.column_checkers = [
            ColumnChecker(name="name", value_type="object"),
            ColumnChecker(name="id", value_type="int"),
            ColumnChecker(name="minutes", value_type="int"),
            ColumnChecker(name="contributor_id", value_type="int"),
            ColumnChecker(
                name="submitted",
                value_type="object",
                check_function=contains_all_dates,
            ),
            ColumnChecker(
                name="tags",
                value_type="object",
                check_function=contains_list_of_strings,
            ),
            ColumnChecker(
                name="nutrition",
                value_type="object",
                check_function=contains_list_of_floats,
            ),
            ColumnChecker(name="n_steps", value_type="int"),
            ColumnChecker(
                name="steps",
                value_type="object",
                check_function=contains_list_of_strings,
            ),
            ColumnChecker(name="description", value_type="object"),
            ColumnChecker(
                name="ingredients",
                value_type="object",
                check_function=contains_list_of_strings,
            ),
            ColumnChecker(name="n_ingredients", value_type="int"),
        ]

    def _additional_checks(self) -> None:
        """Function to add additional checks."""
        try:
            check_array_str_lengths(
                data=self.data,
                column_arrays_name="steps",
                column_control_numbers_name="n_steps",
            )
            check_array_str_lengths(
                data=self.data,
                column_arrays_name="ingredients",
                column_control_numbers_name="n_ingredients",
            )
        except IndexError as e:
            raise ArrayLengthMismatchControlNumberError(
                message=e,
                file_path=f"{self.file_path}",
            )
