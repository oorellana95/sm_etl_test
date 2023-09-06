"""
ProcessFile Class
"""

from abc import ABC

import pandas as pd

from etl.tools.logger import Logger
from exceptions.file_processing_validation_exception import (
    ColumnsNotFoundException,
    ColumnTypeException,
    FileFormatNotAccepted,
    FileIsEmpty,
)


class ProcessFile(ABC):
    def __init__(self):
        self.column_checkers = None
        self.file_type = None
        self.file_path = None
        self.data = None

    def get_data(self) -> pd.DataFrame:
        """Retrieves the data from different types of files to a pandas dataframe."""
        if self.file_type == "xlsx" or self.file_type == "xls":
            self.data = pd.read_excel(self.file_path)
        elif self.file_type == "csv":
            self.data = pd.read_csv(self.file_path)
        else:
            raise FileFormatNotAccepted(
                message=f"File format not accepted: {self.file_type}. Only accepted CSV, XLSX and XLS formats",
                file_path=f"{self.file_path}",
            )

        if self.data is None:
            raise FileIsEmpty(message=f"File is empty", file_path=f"{self.file_path}")
        Logger.info(f"Data retrieved correctly from the file {self.file_path}")
        return self.data

    def get_checked_data(self) -> pd.DataFrame:
        """Returns the data with all checks passed"""
        if self.data is None:
            self.get_data()

        self._check_data_quality()
        return self.data

    def _check_data_quality(self) -> None:
        """Checks if the dataframe has the expected structure and data types."""
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
                raise ColumnsNotFoundException(
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
                raise ColumnTypeException(
                    message=f"From column: {column_checker.name}. Column type should be: {column_checker.value_type}. "
                    f"But is of type: {df_column.dtype}",
                    file_path=f"{self.file_path}",
                )
            if column_checker.check_function:
                try:
                    column_checker.check_function(df_column)
                except ValueError as e:
                    raise ColumnTypeException(
                        message=f"From column {column_checker.name}. {e}",
                        file_path=f"{self.file_path}",
                    )

    def _additional_checks(self) -> None:
        """Function to add additional checks."""
        pass
