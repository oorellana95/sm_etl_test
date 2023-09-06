from etl.config import RAW_RECIPES_PATH
from etl.process_file.column_checker import ColumnChecker
from etl.process_file.process_file import ProcessFile
from etl.tools.validation_functions import check_contains_all_date, check_contains_list_of_strings, \
    check_contains_list_of_floats


class ProcessFileRecipes(ProcessFile):
    def __init__(self):
        super().__init__()
        self.file_type = "csv"
        self.file_path = RAW_RECIPES_PATH
        self.column_checkers = [
            ColumnChecker(name="name", value_type="object", check_function=None),
            ColumnChecker(name="id", value_type="int", check_function=None),
            ColumnChecker(name="minutes", value_type="int", check_function=None),
            ColumnChecker(name="contributor_id", value_type="int", check_function=None),
            ColumnChecker(name="submitted", value_type="object", check_function=check_contains_all_date),
            ColumnChecker(name="tags", value_type="object", check_function=check_contains_list_of_strings),
            ColumnChecker(name="nutrition", value_type="object", check_function=check_contains_list_of_floats),
            ColumnChecker(name="n_steps", value_type="int", check_function=None),
            ColumnChecker(name="steps", value_type="object", check_function=check_contains_list_of_strings),
            ColumnChecker(name="description", value_type="object", check_function=None),
            ColumnChecker(name="ingredients", value_type="object", check_function=check_contains_list_of_strings),
            ColumnChecker(name="n_ingredients", value_type="int", check_function=None)
        ]
