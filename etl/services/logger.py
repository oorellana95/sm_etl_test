"""
Logger Class
"""
import logging

from etl.config import PROJECT_NAME, SERVICE_NAME


class Logger:
    _project = PROJECT_NAME
    _service = SERVICE_NAME
    _logger = logging.getLogger(__name__)

    def __new__(cls):
        return cls

    @classmethod
    def error(cls, message: str, code: str = None, additional_information: dict = None):
        """Log an error message with the standard output format."""
        cls._logger.setLevel(logging.ERROR)
        output = cls.output(
            logger_type="Error",
            message=message,
            code=code,
            additional_information=additional_information,
        )
        cls._logger.error(output)

    @classmethod
    def warning(
        cls, message: str, code: str = None, additional_information: dict = None
    ):
        """Log a warning message with the standard output format."""
        cls._logger.setLevel(logging.WARNING)
        output = cls.output(
            logger_type="Warning",
            message=message,
            code=code,
            additional_information=additional_information,
        )
        cls._logger.warning(output)

    @classmethod
    def debug(cls, message: str, code: str = None, additional_information: dict = None):
        """Log a debug message with the standard output format."""
        cls._logger.setLevel(logging.DEBUG)
        output = cls.output(
            logger_type="Debug",
            message=message,
            code=code,
            additional_information=additional_information,
        )
        cls._logger.debug(output)

    @classmethod
    def info(cls, message: str, code: str = None, additional_information: dict = None):
        """Log an information message with the standard output format."""
        cls._logger.setLevel(logging.INFO)
        output = cls.output(
            logger_type="Info",
            message=message,
            code=code,
            additional_information=additional_information,
        )
        cls._logger.info(output)

    @classmethod
    def output(
        cls, logger_type: str, message: str, code: str, additional_information: dict
    ):
        """Output message with code and value."""
        output = f"{logger_type} in {cls._project}:{cls._service};"
        if code:
            output = output + f"\n{logger_type} code: {code};"
        if additional_information:
            output = output + f"\n{additional_information};"
        return output + f"\nMessage: {message}"
