"""Sm Etl Test Exception Class"""


class SmEtlTestException(Exception):
    def __init__(self):
        self.code = None
        self.message = None
        self.additional_information = {}
