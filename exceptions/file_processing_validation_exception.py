"""File Processing Validation Exception Classes"""
from exceptions.sm_etl_test_exception import SmEtlTestException


class FileProcessingValidationException(SmEtlTestException):
    def __init__(self):
        super().__init__()
        self.code = "ERROR.FILE_PROCESSING_VALIDATION"


class FileFormatNotAccepted(FileProcessingValidationException):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs


class FileIsEmpty(FileProcessingValidationException):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs


class ColumnsNotFoundException(FileProcessingValidationException):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs


class ColumnTypeException(FileProcessingValidationException):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs


class ArrayLengthMismatchControlNumberError(FileProcessingValidationException):
    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.additional_information = kwargs
