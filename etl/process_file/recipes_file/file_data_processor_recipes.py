"""
FileDataProcessorRecipes Class
Custom class inherited from the FileDataProcessor Class with the Interactions specifications to process the file.
"""
from etl.config import config
from etl.exceptions.file_processing_exeptions.extract_validation_file_processing_error import (
    ArrayLengthMismatchControlNumberError,
)
from etl.process_file.column_checker import ColumnChecker
from etl.process_file.file_data_processor import FileDataProcessor
from etl.process_file.recipes_file.ingredients.ingredient_repository import (
    load_ingredients,
)
from etl.process_file.recipes_file.recipe_repository import load_recipes
from etl.process_file.recipes_file.tags.tag_repository import load_tags
from etl.services.general_functions.list_evaluation_utils import (
    evaluate_and_flatten_nested_lists_with_error_handling,
)
from etl.services.general_functions.validation import (
    contains_all_dates,
    contains_list_of_floats,
    contains_list_of_strings,
)
from etl.services.logger import Logger
from etl.services.pandas.validation import check_array_str_lengths


class FileDataProcessorRecipes(FileDataProcessor):
    def __init__(self, db_session):
        super().__init__(db_session)
        self.file_type = "csv"
        self.file_path = config.files_config["RAW_RECIPES_CSV_PATH"]
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
        """Load data from the file, creating and updating tags, ingredients, recipes_file and its relationships"""
        # Load tags
        Logger.info(message=f"Loading tags...")
        tags = evaluate_and_flatten_nested_lists_with_error_handling(
            self.data["tags"]
        ).get(
            "flattened_list"
        )  # TODO handle errors related with tags

        load_tags(db_session=self.db_session, tags=tags)
        Logger.info(message=f"Tags loaded successfully")

        # Load ingredients
        Logger.info(message=f"Loading ingredients...")
        ingredients = evaluate_and_flatten_nested_lists_with_error_handling(
            self.data["ingredients"]
        ).get(
            "flattened_list"
        )  # TODO handle errors related with the ingredients
        load_ingredients(db_session=self.db_session, ingredients=ingredients)
        Logger.info(message=f"Ingredients loaded successfully")

        # Load recipes_file and associative tables (recipe_tag, recipe_ingredient)
        Logger.info(message=f"Loading recipes and associated data...")
        load_recipes(db_session=self.db_session, recipes_df=self.data)
        Logger.info(message=f"Recipes and associated data loaded successfully")
