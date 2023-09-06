"""
ProcessFileUsers Class
Custom class inherited from the ProcessFile Class with the Interactions specifications to process the file.
"""

from etl.config import RAW_USERS_PATH
from etl.process_file.column_checker import ColumnChecker
from etl.process_file.file_data_processor import FileDataProcessor
from etl.tools.validation_functions.general_functions import (
    contains_all_dates,
    contains_list_of_emails,
    contains_list_of_sex_values,
)


class FileDataProcessorUsers(FileDataProcessor):
    def __init__(self):
        super().__init__()
        self.file_type = "csv"
        self.file_path = RAW_USERS_PATH
        self.column_checkers = [
            ColumnChecker(name="user id", value_type="int", check_function=None),
            ColumnChecker(name="encoded id", value_type="object", check_function=None),
            ColumnChecker(name="first name", value_type="object", check_function=None),
            ColumnChecker(name="last name", value_type="object", check_function=None),
            ColumnChecker(
                name="Sex",
                value_type="object",
                check_function=contains_list_of_sex_values,
            ),
            ColumnChecker(
                name="email",
                value_type="object",
                check_function=contains_list_of_emails,
            ),
            ColumnChecker(name="phone", value_type="object", check_function=None),
            ColumnChecker(
                name="date of birth",
                value_type="object",
                check_function=contains_all_dates,
            ),
            ColumnChecker(name="job title", value_type="object", check_function=None),
        ]
