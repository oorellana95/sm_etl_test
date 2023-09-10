import configparser
import os


class Config:
    general_config = None
    database_config = None
    files_config = None

    def __init__(self):
        self.load_ini_config()

    def load_ini_config(self):
        _config = configparser.ConfigParser()
        _config.read("config.ini")

        self.general_config = {
            "PROJECT_NAME": _config.get("general", "project_name"),
            "SERVICE_NAME": _config.get("general", "service_name"),
            "LOGGER_LEVEL": _config.get("general", "logger_level"),
            "ENVIRONMENT": _config.get("general", "environment"),
        }

        self.database_config = {
            "DATABASE_DIALECT": _config.get("database", "dialect"),
            "DATABASE_HOST": _config.get("database", "host"),
            "DATABASE_PORT": int(_config.get("database", "port")),
            "DATABASE_USER": _config.get("database", "user"),
            "DATABASE_PASSWORD": _config.get("database", "password"),
            "DATABASE_NAME": _config.get("database", "name"),
            "DATABASE_BATCH_SIZE": int(_config.get("database", "batch_size")),
        }

        if self.general_config["ENVIRONMENT"] in ("local", "test"):
            working_dir_path = os.path.abspath("")
            input_dir_path = os.path.join(
                working_dir_path, f"data_{self.general_config['ENVIRONMENT']}/input"
            )
            self.files_config = {
                "RAW_USERS_CSV_PATH": os.path.join(input_dir_path, "RAW_users.csv"),
                "RAW_RECIPES_CSV_PATH": os.path.join(input_dir_path, "RAW_recipes.csv"),
                "RAW_INTERACTIONS_CSV_PATH": os.path.join(
                    input_dir_path, "RAW_interactions.csv"
                ),
                "ERROR_OUTPUT_DIR_PATH": os.path.join(
                    working_dir_path,
                    f"data_{self.general_config['ENVIRONMENT']}/output",
                ),
            }
        else:
            self.files_config = {
                "RAW_USERS_CSV_PATH": _config.get("files", "raw_users_csv_path"),
                "RAW_RECIPES_CSV_PATH": _config.get("files", "raw_recipes_csv_path"),
                "RAW_INTERACTIONS_CSV_PATH": int(
                    _config.get("files", "raw_interactions_csv_path")
                ),
                "ERROR_OUTPUT_DIR_PATH": _config.get("files", "error_output_dir_path"),
            }


# Create a global instance of the Config class
config = Config()
