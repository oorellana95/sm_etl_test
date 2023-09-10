import pytest

from etl.exceptions.file_processing_exeptions.database_load_file_processing_error import \
    DatabaseLoadFileProcessingError, DatabaseTransactionError
from etl.exceptions.file_processing_exeptions.extract_validation_file_processing_error import \
    ExtractValidationFileProcessingError, FileFormatNotAcceptedError, FileIsEmptyError, ColumnsNotFoundError, \
    ColumnTypeError, ArrayLengthMismatchControlNumberError
from etl.exceptions.file_processing_exeptions.file_processing_error import FileProcessingError
from etl.exceptions.sm_etl_test_exception import SmEtlTestException


def test_sm_etl_test_exception():
    with pytest.raises(SmEtlTestException):
        raise SmEtlTestException()


def test_file_processing_error():
    with pytest.raises(FileProcessingError):
        raise FileProcessingError()


def test_extract_validation_file_processing_error():
    with pytest.raises(ExtractValidationFileProcessingError):
        raise ExtractValidationFileProcessingError()


def test_file_format_not_accepted_error():
    message = "File format not accepted"
    with pytest.raises(FileFormatNotAcceptedError) as excinfo:
        raise FileFormatNotAcceptedError(message)
    assert str(excinfo.value) == message


def test_file_is_empty_error():
    message = "File is empty"
    with pytest.raises(FileIsEmptyError) as excinfo:
        raise FileIsEmptyError(message)
    assert str(excinfo.value) == message


def test_columns_not_found_error():
    message = "Columns not found"
    with pytest.raises(ColumnsNotFoundError) as excinfo:
        raise ColumnsNotFoundError(message)
    assert str(excinfo.value) == message


def test_column_type_error():
    message = "Column type error"
    with pytest.raises(ColumnTypeError) as excinfo:
        raise ColumnTypeError(message)
    assert str(excinfo.value) == message


def test_array_length_mismatch_control_number_error():
    message = "Array length mismatch control number error"
    with pytest.raises(ArrayLengthMismatchControlNumberError) as excinfo:
        raise ArrayLengthMismatchControlNumberError(message)
    assert str(excinfo.value) == message


def test_database_load_file_processing_error():
    with pytest.raises(DatabaseLoadFileProcessingError):
        raise DatabaseLoadFileProcessingError()


def test_database_transaction_error():
    message = "Database transaction error"
    additional_info = {"key1": "value1", "key2": "value2"}
    with pytest.raises(DatabaseTransactionError) as excinfo:
        raise DatabaseTransactionError(message, additional_information=additional_info)
    assert str(excinfo.value) == message
    assert excinfo.value.additional_information == {'additional_information': {'key1': 'value1', 'key2': 'value2'}}


def test_set_additional_information():
    error = DatabaseTransactionError("Database transaction error")
    new_info = {"new_key": "new_value"}
    error.set_additional_information(**new_info)
    assert error.additional_information == new_info
