from etl.exceptions.sm_etl_test_exception import SmEtlTestException
from etl.process_file.file_data_processor_interactions import (
    FileDataProcessorInteractions,
)
from etl.process_file.file_data_processor_recipes import FileDataProcessorRecipes
from etl.process_file.file_data_processor_users import FileDataProcessorUsers
from etl.services.database import create_database_session
from etl.services.logger import Logger

if __name__ == "__main__":
    with create_database_session() as db:
        try:
            Logger.info(message="Starting process to extract, check and load database")
            FileDataProcessorUsers(db_session=db).execute()
            FileDataProcessorRecipes(db_session=db).execute()
            FileDataProcessorInteractions(db_session=db).execute()
            Logger.info(message="All files have been processed successfully")
        except SmEtlTestException as e:
            Logger.error(
                message=e.message,
                code=e.code,
                additional_information=e.additional_information,
                multiple_errors=e.multiple_errors,
            )
            raise
        except Exception as e:
            Logger.error(
                message=f"An uncontrolled exception occurred: {e}",
                code="UNCONTROLLED EXCEPTION",
            )
            raise
