"""
FileDataProcessorInteractions Class
Custom class inherited from the FileDataProcessor Class with the Interactions specifications to process the file.
"""
from etl.config import config
from etl.process_file.column_checker import ColumnChecker
from etl.process_file.file_data_processor import FileDataProcessor
from etl.process_file.interactions_file.rating_repository import load_ratings
from etl.services.general_functions.validation import (
    contains_all_dates,
    contains_all_valid_ranking_numbers,
)
from etl.services.logger import Logger


class FileDataProcessorInteractions(FileDataProcessor):
    def __init__(self, db_session):
        super().__init__(db_session)
        self.file_type = "csv"
        self.file_path = config.files_config["RAW_INTERACTIONS_CSV_PATH"]
        self.column_checkers = [
            ColumnChecker(name="user_id", value_type="int"),
            ColumnChecker(name="recipe_id", value_type="int"),
            ColumnChecker(
                name="date", value_type="object", check_function=contains_all_dates
            ),
            ColumnChecker(
                name="rating",
                value_type="int",
                check_function=contains_all_valid_ranking_numbers,
            ),
            ColumnChecker(name="review", value_type="object", check_function=None),
        ]

    def load_data(self):
        """Load data from the file, creating and updating job_titles and users_file"""
        Logger.info(message=f"Loading ratings...")
        load_ratings(db_session=self.db_session, ratings_df=self.data)
        Logger.info(message=f"Ratings loaded successfully")
