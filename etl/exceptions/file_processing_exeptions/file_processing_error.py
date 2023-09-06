"""File Processing Validation Exception Classes"""
from etl.exceptions.sm_etl_test_exception import SmEtlTestException


class FileProcessingError(SmEtlTestException):
    def __init__(self):
        super().__init__()
        self.code = "ERROR.FILE_PROCESSING"
