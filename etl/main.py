from etl.process_file.file_data_processor_interactions import (
    FileDataProcessorInteractions,
)
from etl.process_file.file_data_processor_recipes import FileDataProcessorRecipes
from etl.process_file.file_data_processor_users import FileDataProcessorUsers
from etl.tools.logger import Logger
from exceptions.sm_etl_test_exception import SmEtlTestException

if __name__ == "__main__":
    try:
        FileDataProcessorInteractions().execute()
        FileDataProcessorRecipes().execute()
        FileDataProcessorUsers().execute()
        Logger.info(f"All data files has been processed correctly :)")
    except SmEtlTestException as e:
        Logger.error(
            message=e.message,
            code=e.code,
            additional_information=e.additional_information,
        )
