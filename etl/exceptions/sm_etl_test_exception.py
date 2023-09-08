"""
SmEtlTestException Class.
This is the main exception class for the SmEtlTest project. All custom exceptions should inherit from this class.
"""


class SmEtlTestException(Exception):
    def __init__(self):
        self.code = None
        self.message = None
        self.additional_information = {}
        self.multiple_errors = None
