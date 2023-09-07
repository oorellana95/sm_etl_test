"""
ColumnChecker Class
Creates a standardized class for dataframe checking purposes.
"""
from typing import Any, Optional


class ColumnChecker:
    def __init__(
        self, name: str, value_type: str, check_function: Optional[Any] = None
    ):
        self.name = name
        self.value_type = value_type  # Note, it follows the pandas dtype convention. object = str or mixed
        self.check_function = check_function
