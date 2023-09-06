"""
ProcessFile Class
"""

from abc import ABC

import pandas as pd

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
        # self._check_data()
        self._load_data()

    def _extract_data(self) -> pd.DataFrame:
        """Extracts the data from different types of files and returns a pandas dataframe."""
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
        """Checks if the dataframe has, at least, the expected structure and data types."""
        self._check_mandatory_columns()
        self._check_data_from_columns()
        self._additional_checks()
        Logger.info(f"All quality checks have passed for the file: {self.file_path}")

    def _check_mandatory_columns(self) -> None:
        """Raise an input validation error if there are mandatory columns missing."""
        mandatory_columns = set([column.name for column in self.column_checkers])
        current_columns = set(self.data.columns)

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
        """Raise an input validation error if there are column types not expected."""
        for column_checker in self.column_checkers:
            df_column = self.data[column_checker.name]
            is_same_type = pd.api.types.is_dtype_equal(
                column_checker.value_type, df_column.dtype
            )
            if not is_same_type:
                raise ColumnTypeError(
                    message=f"From column: {column_checker.name}. Column type should be: {column_checker.value_type}. "
                    f"But is of type: {df_column.dtype}",
                    file_path=f"{self.file_path}",
                )
            if column_checker.check_function:
                try:
                    column_checker.check_function(df_column)
                except ValueError as e:
                    raise ColumnTypeError(
                        message=f"From column {column_checker.name}. {e}",
                        file_path=f"{self.file_path}",
                    )

    def _additional_checks(self) -> None:
        """Function to add additional checks."""
        pass

    def _load_data(self) -> None:
        """Function to load the data to the database."""
        pass
