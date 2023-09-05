"""Logger Class"""
import logging


class Logger:
    _project = "sm_etl_test"
    _service = "ETL Service"
    _logger = logging.getLogger(__name__)

    def __new__(cls):
        return cls

    @classmethod
    def error(cls, message: str, code: str = None):
        """Log an error message with the standard output format."""
        cls._logger.setLevel(logging.ERROR)
        output = cls.output(logger_type="Error", message=message, code=code)
        cls._logger.error(output)

    @classmethod
    def warning(cls, message: str, code: str = None):
        """Log a warning message with the standard output format."""
        cls._logger.setLevel(logging.WARNING)
        output = cls.output(logger_type="Warning", message=message, code=code)
        cls._logger.warning(output)

    @classmethod
    def debug(cls, message: str, code: str = None):
        """Log a debug message with the standard output format."""
        cls._logger.setLevel(logging.DEBUG)
        output = cls.output(logger_type="Debug", message=message, code=code)
        cls._logger.debug(output)

    @classmethod
    def info(cls, message: str, code: str = None):
        """Log an information message with the standard output format."""
        cls._logger.setLevel(logging.INFO)
        output = cls.output(logger_type="Info", message=message, code=code)
        cls._logger.info(output)

    @classmethod
    def output(cls, logger_type: str, message: str, code: str):
        """Output message with code and value."""
        output = f"{logger_type} in {cls._project}:{cls._service};"
        if code:
            output = output + f"\n{logger_type} code: {code};"
        return output + f"\nMessage: {message}"
