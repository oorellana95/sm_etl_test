from etl.process_file.process_file_interactions import ProcessFileInteractions
from etl.tools.logger import Logger
from exceptions.sm_etl_test_exception import SmEtlTestException

if __name__ == "__main__":
    # Improve the way of calling the items
    try:
        interactions_data = ProcessFileInteractions().get_checked_data()
        print("Hello World :)")
    except SmEtlTestException as e:
        Logger.error(
            message=e.message,
            code=e.code,
            additional_information=e.additional_information,
        )
