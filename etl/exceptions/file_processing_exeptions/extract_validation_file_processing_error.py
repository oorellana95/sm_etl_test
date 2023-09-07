"""
ExtractValidationFileProcessingError Classes
This module defines custom exception classes for handling errors that occur during the extraction and validation of
files in the SmEtlTest project.
"""
from etl.exceptions.file_processing_exeptions.file_processing_error import (
    FileProcessingError,
)


class ExtractValidationFileProcessingError(FileProcessingError):
    def __init__(self):
        super().__init__()
        self.code = f"{self.code}.EXTRACT_VALIDATION"


class FileFormatNotAcceptedError(ExtractValidationFileProcessingError):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs


class FileIsEmptyError(ExtractValidationFileProcessingError):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs


class ColumnsNotFoundError(ExtractValidationFileProcessingError):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs


class ColumnTypeError(ExtractValidationFileProcessingError):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs


class ArrayLengthMismatchControlNumberError(ExtractValidationFileProcessingError):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs
