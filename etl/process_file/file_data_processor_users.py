"""
ProcessFileUsers Class
Custom class inherited from the ProcessFile Class with the Interactions specifications to process the file.
"""

from etl.config import RAW_USERS_PATH
from etl.exceptions.file_processing_exeptions.database_load_file_processing_error import (
    DatabaseLoadFileProcessingError,
)
from etl.models.job_title import JobTitle
from etl.process_file.column_checker import ColumnChecker
from etl.process_file.file_data_processor import FileDataProcessor
from etl.tools.validation_functions.general_functions import (
    contains_all_dates,
    contains_list_of_emails,
    contains_list_of_sex_values,
)


class FileDataProcessorUsers(FileDataProcessor):
    def __init__(self, db_session):
        super().__init__(db_session)
        self.file_type = "csv"
        self.file_path = RAW_USERS_PATH
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

    def _load_data(self):
        self.load_job_titles()

    def _load_job_titles(self):
        job_titles_from_file = set(self.data["job title"].unique())
        job_titles_from_database = set(
            [job_title.name for job_title in self.db_session.query(JobTitle).all()]
        )
        missing_job_titles = job_titles_from_file - job_titles_from_database

        if missing_job_titles:
            try:
                for new_job_title in missing_job_titles:
                    new_row = JobTitle(name=new_job_title)
                    self.db_session.add(new_row)
                self.db_session.commit()
            except Exception as e:
                self.db_session.rollback()
                raise DatabaseLoadFileProcessingError(
                    message=f"An error occurred while loading job titles {e}",
                    file_path=f"{self.file_path}",
                    database_url=self.db_session.bind.url,
                )
