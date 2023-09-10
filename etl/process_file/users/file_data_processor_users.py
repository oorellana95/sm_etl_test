"""
FileDataProcessorUsers Class
Custom class inherited from the FileDataProcessor Class with the Interactions specifications to process the file.
"""
from etl.config import config
from etl.process_file.column_checker import ColumnChecker
from etl.process_file.file_data_processor import FileDataProcessor
from etl.process_file.users.job_title.job_title_repository import load_job_titles
from etl.process_file.users.user_repository import load_users
from etl.services.general_functions.validation import (
    contains_all_dates,
    contains_list_of_emails,
    contains_list_of_sex_values,
)
from etl.services.logger import Logger


class FileDataProcessorUsers(FileDataProcessor):
    def __init__(self, db_session):
        super().__init__(db_session)
        self.file_type = "csv"
        self.file_path = config.files_config["RAW_USERS_CSV_PATH"]
        self.column_checkers = [
            ColumnChecker(name="user id", value_type="int"),
            ColumnChecker(name="encoded id", value_type="object"),
            ColumnChecker(name="first name", value_type="object"),
            ColumnChecker(name="last name", value_type="object"),
            ColumnChecker(
                name="Sex",
                value_type="object",
                check_function=contains_list_of_sex_values,
            ),
            ColumnChecker(
                name="email",
                value_type="object",
                check_function=contains_list_of_emails,
            ),
            ColumnChecker(name="phone", value_type="object"),
            ColumnChecker(
                name="date of birth",
                value_type="object",
                check_function=contains_all_dates,
            ),
            ColumnChecker(name="job title", value_type="object"),
        ]

    def load_data(self):
        """Load data from the file, creating and updating job_titles and users"""
        # Load job titles
        Logger.info(message=f"Loading job titles...")
        load_job_titles(
            db_session=self.db_session, job_titles=self.data["job title"].unique()
        )
        Logger.info(message=f"Job titles loaded successfully")

        # Load users
        Logger.info(message=f"Loading users...")
        load_users(db_session=self.db_session, users_df=self.data)
        Logger.info(message=f"Users loaded successfully")
