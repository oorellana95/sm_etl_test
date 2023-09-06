from etl.process_file.file_data_processor_interactions import FileDataProcessorInteractions
from etl.process_file.file_data_processor_recipes import FileDataProcessorRecipes
from etl.process_file.file_data_processor_users import FileDataProcessorUsers
from etl.tools.logger import Logger
from exceptions.sm_etl_test_exception import SmEtlTestException

if __name__ == "__main__":
    # Improve the way of calling the items
    try:
        interactions_data = FileDataProcessorInteractions().get_checked_data()
        recipes_data = FileDataProcessorRecipes().get_checked_data()
        users_data = FileDataProcessorUsers().get_checked_data()
        print("Hello World :)")
    except SmEtlTestException as e:
        Logger.error(
            message=e.message,
            code=e.code,
            additional_information=e.additional_information,
        )
