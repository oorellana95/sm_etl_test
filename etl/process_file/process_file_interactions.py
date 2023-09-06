"""
ProcessFileInteractions Class
Custom class inherited from the ProcessFile Class with the Interactions specifications to process the file.
"""

from etl.config import RAW_INTERACTIONS_PATH
from etl.process_file.column_checker import ColumnChecker
from etl.process_file.process_file import ProcessFile
from etl.tools.validation_functions.general_functions import (
    contains_all_dates,
    contains_all_valid_ranking_numbers,
)


class ProcessFileInteractions(ProcessFile):
    def __init__(self):
        super().__init__()
        self.file_type = "csv"
        self.file_path = RAW_INTERACTIONS_PATH
        self.column_checkers = [
            ColumnChecker(name="user_id", value_type="int", check_function=None),
            ColumnChecker(name="recipe_id", value_type="int", check_function=None),
            ColumnChecker(
                name="date", value_type="object", check_function=contains_all_dates
            ),
            ColumnChecker(
                name="rating",
                value_type="int",
                check_function=contains_all_valid_ranking_numbers,
            ),
            ColumnChecker(name="review", value_type="object", check_function=None),
        ]
