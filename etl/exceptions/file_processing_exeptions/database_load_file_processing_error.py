"""File Processing Validation Exception Classes"""
from etl.exceptions.file_processing_exeptions.file_processing_error import (
    FileProcessingError,
)


class DatabaseLoadFileProcessingError(FileProcessingError):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.code = f"{self.code}.DATABASE_LOAD"
        self.message = message
        self.additional_information = kwargs
