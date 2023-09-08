"""
DatabaseLoadFileProcessingError Classes
This exception class is used to represent errors that occur during the database load process when processing files in
the context of the SmEtlTest project.
"""
from etl.exceptions.file_processing_exeptions.file_processing_error import (
    FileProcessingError,
)


class DatabaseLoadFileProcessingError(FileProcessingError):
    def __init__(self, **kwargs):
        super().__init__()
        self.code = f"{self.code}.DATABASE_LOAD"


class DatabaseTransactionError(DatabaseLoadFileProcessingError):
    def __init__(self, message, multiple_errors=None, **additional_information):
        super().__init__()
        self.message = message
        self.multiple_errors = multiple_errors
        self.additional_information = additional_information

    def set_additional_information(self, **new_information):
        self.additional_information.update(new_information)
