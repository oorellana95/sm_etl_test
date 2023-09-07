"""
FileDataProcessor Class
Main class to inherit from with the intention to process files, extracting, checking and loading the data.
"""

from abc import ABC

import pandas as pd

from etl.exceptions.file_processing_exeptions.database_load_file_processing_error import (
    DatabaseLoadFileProcessingError,
)
from etl.exceptions.file_processing_exeptions.extract_validation_file_processing_error import (
    ColumnsNotFoundError,
    ColumnTypeError,
    FileFormatNotAcceptedError,
    FileIsEmptyError,
)
from etl.services.logger import Logger


class FileDataProcessor(ABC):
    def __init__(self, db_session):
        self.db_session = db_session
        self.column_checkers = None
        self.file_type = None
        self.file_path = None
        self.data = None

    def execute(self):
        """Extract, check and loads the data to the database."""
        self._extract_data()
        self._check_data()
        self._load_data()

    def _extract_data(self) -> pd.DataFrame:
        """Extracts the data accordingly checking the file type."""
        if self.file_type == "xlsx" or self.file_type == "xls":
            self.data = pd.read_excel(self.file_path)
        elif self.file_type == "csv":
            self.data = pd.read_csv(self.file_path)
        else:
            raise FileFormatNotAcceptedError(
                message=f"File format not accepted: {self.file_type}. Only accepted CSV, XLSX and XLS formats",
                file_path=f"{self.file_path}",
            )

        if self.data is None:
            raise FileIsEmptyError(
                message=f"File is empty", file_path=f"{self.file_path}"
            )
        Logger.info(f"Data retrieved correctly from the file {self.file_path}")
        return self.data

    def _check_data(self) -> None:
        """Check if the dataframe has the expected structure and data types."""
        self._check_mandatory_columns()
        self._check_data_from_columns()
        self.additional_checks()
        Logger.info(f"All quality checks have passed for the file: {self.file_path}")

    def _check_mandatory_columns(self) -> None:
        """Raise an input validation error if there are mandatory columns missing."""
        mandatory_columns = set([column.name for column in self.column_checkers])
        current_columns = set(self.data.columns)

        # Check if the sets of mandatory and current columns match
        if mandatory_columns != current_columns:
            missing_mandatory_columns = mandatory_columns - current_columns
            if missing_mandatory_columns:
                raise ColumnsNotFoundError(
                    message=f"Missing columns: {missing_mandatory_columns}. They are mandatory",
                    file_path=f"{self.file_path}",
                )
            else:
                Logger.warning(
                    f"The file {self.file_path} has more columns than expected. The additional columns are: {current_columns - mandatory_columns}"
                )

    def _check_data_from_columns(self) -> None:
        """Raise an input validation error if there are unexpected column types or check function errors."""
        for column_checker in self.column_checkers:
            column_name = column_checker.name
            expected_type = column_checker.value_type
            df_column = self.data[column_name]

            # Check if the actual column type matches the expected type
            if not pd.api.types.is_dtype_equal(expected_type, df_column.dtype):
                message = f"Column '{column_name}' should have type '{expected_type}' but is of type '{df_column.dtype}'."
                raise ColumnTypeError(message=message, file_path=self.file_path)

            # If a custom check function is provided, execute it and handle any exceptions
            if column_checker.check_function:
                try:
                    column_checker.check_function(df_column)
                except ValueError as e:
                    message = f"Error in column '{column_name}': {e}"
                    raise ColumnTypeError(message=message, file_path=self.file_path)

    def _load_data(self) -> None:
        """Attempt to load data into the database and handle exceptions."""
        try:
            # Call the custom load_data method to load data into the database
            self.load_data()
        except Exception as e:
            raise DatabaseLoadFileProcessingError(
                message=f"An error occurred while loading data. {e}",
                file_path=self.file_path,
                database_url=self.db_session.bind.url,
            )

    def additional_checks(self) -> None:
        """Function to add additional checks."""
        pass

    def load_data(self) -> None:
        """Function to load data into the database."""
        pass
