from etl.exceptions.sm_etl_test_exception import SmEtlTestException
from etl.process_file.file_data_processor_users import FileDataProcessorUsers
from etl.services.database import create_database_session
from etl.services.logger import Logger

if __name__ == "__main__":
    with create_database_session() as db:
        try:
            # FileDataProcessorInteractions().execute()
            # FileDataProcessorRecipes().execute()
            FileDataProcessorUsers(db_session=db).execute()
            Logger.info(f"All data files have been processed correctly :)")
        except SmEtlTestException as e:
            Logger.error(
                message=e.message,
                code=e.code,
                additional_information=e.additional_information,
            )
        except Exception as e:
            Logger.error(
                message=e,
                code="UNCONTROLLED EXCEPTION",
            )
