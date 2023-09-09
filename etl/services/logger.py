"""
Logger Class
"""
import logging
from datetime import datetime

from etl.config import PROJECT_NAME, SERVICE_NAME, LOGGER_LEVEL


class Logger:
    logging.basicConfig()
    _logger = logging.getLogger(__name__)
    _logger.setLevel(LOGGER_LEVEL)

    def __new__(cls):
        return cls

    @classmethod
    def error(
        cls,
        message: str,
        code: str = None,
        additional_information: dict = None,
        multiple_errors: dict = None,
    ):
        """Log an error message with the standard output format."""
        output = cls.output(
            logger_type="Error",
            message=message,
            code=code,
            additional_information=additional_information,
            list_items=multiple_errors,
        )
        cls._logger.error(output)

    @classmethod
    def warning(
        cls, message: str, code: str = None, additional_information: dict = None
    ):
        """Log a warning message with the standard output format."""
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
        output = cls.output(
            logger_type="Info",
            message=message,
            code=code,
            additional_information=additional_information,
        )
        cls._logger.info(output)

    @classmethod
    def output(
        cls,
        logger_type: str,
        message: str,
        code: str,
        additional_information: dict,
        list_items: list = None,
    ):
        """Output message with code and value."""
        output = f"{datetime.now()} - {PROJECT_NAME}:{SERVICE_NAME} - "

        if code:
            output = output + f"\n{logger_type} code: {code};\n"

        output += f"{message}"

        if additional_information:
            output = output + f"\nAdditional information: {additional_information};"
        if list_items:
            output = output + f"\nRegistered items:"
            for item in list_items:
                output += f"\n  - {item}"

        return output
