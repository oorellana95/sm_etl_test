"""
FileDataProcessorRecipes Class
Custom class inherited from the FileDataProcessor Class with the Interactions specifications to process the file.
"""
from etl.config import RAW_RECIPES_PATH
from etl.exceptions.file_processing_exeptions.extract_validation_file_processing_error import (
    ArrayLengthMismatchControlNumberError,
)
from etl.process_file.column_checker import ColumnChecker
from etl.process_file.file_data_processor import FileDataProcessor
from etl.repositories.recipe import load_recipes
from etl.repositories.unique_name_table import load_ingredients, load_tags
from etl.tools.functions.general.list_evaluation_utils import (
    evaluate_and_flatten_nested_lists,
)
from etl.tools.functions.general.validation import (
    contains_all_dates,
    contains_list_of_floats,
    contains_list_of_strings,
)
from etl.tools.functions.pandas.validation import check_array_str_lengths


class FileDataProcessorRecipes(FileDataProcessor):
    def __init__(self, db_session):
        super().__init__(db_session)
        self.file_type = "csv"
        self.file_path = RAW_RECIPES_PATH
        self.column_checkers = [
            ColumnChecker(name="name", value_type="object"),
            ColumnChecker(name="id", value_type="int"),
            ColumnChecker(name="minutes", value_type="int"),
            ColumnChecker(name="contributor_id", value_type="int"),
            ColumnChecker(
                name="submitted",
                value_type="object",
                check_function=contains_all_dates,
            ),
            ColumnChecker(
                name="tags",
                value_type="object",
                check_function=contains_list_of_strings,
            ),
            ColumnChecker(
                name="nutrition",
                value_type="object",
                check_function=contains_list_of_floats,
            ),
            ColumnChecker(name="n_steps", value_type="int"),
            ColumnChecker(
                name="steps",
                value_type="object",
                check_function=contains_list_of_strings,
            ),
            ColumnChecker(name="description", value_type="object"),
            ColumnChecker(
                name="ingredients",
                value_type="object",
                check_function=contains_list_of_strings,
            ),
            ColumnChecker(name="n_ingredients", value_type="int"),
        ]

    def additional_checks(self) -> None:
        """Function to add additional checks."""
        try:
            check_array_str_lengths(
                data=self.data,
                column_arrays_name="steps",
                column_control_numbers_name="n_steps",
            )
            check_array_str_lengths(
                data=self.data,
                column_arrays_name="ingredients",
                column_control_numbers_name="n_ingredients",
            )
        except IndexError as e:
            raise ArrayLengthMismatchControlNumberError(
                message=e,
                file_path=f"{self.file_path}",
            )

    def load_data(self):
        """Load data from the file, creating and updating tags, ingredients, recipes and its relationships"""
        tags = evaluate_and_flatten_nested_lists(self.data["tags"])
        load_tags(db_session=self.db_session, tags=tags)

        ingredients = evaluate_and_flatten_nested_lists(self.data["ingredients"])
        load_ingredients(db_session=self.db_session, ingredients=ingredients)

        load_recipes(db_session=self.db_session, recipes_df=self.data)
