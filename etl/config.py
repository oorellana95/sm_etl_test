import os

# Critical values should be SECRETS.

# General
PROJECT_NAME: str = "sm_etl_test"
SERVICE_NAME: str = "ETL_Service"

# Files
PATH_ROOT_DIR = os.path.abspath("")
PATH_INPUT_DIR = os.path.join(PATH_ROOT_DIR, "data_test/input")
RAW_USERS_PATH = os.path.join(PATH_INPUT_DIR, "RAW_users.csv")
RAW_RECIPES_PATH = os.path.join(PATH_INPUT_DIR, "RAW_recipes.csv")
RAW_INTERACTIONS_PATH = os.path.join(PATH_INPUT_DIR, "RAW_interactions.csv")

PATH_OUTPUT_DIR = os.path.join(PATH_ROOT_DIR, "data_test/output")

# Database
DATABASE_DIALECT: str = "mysql+pymysql"
DATABASE_HOST: str = "localhost"
DATABASE_PORT: int = 3306
DATABASE_USER: str = "master"
DATABASE_PASSWORD: str = "pass"
DATABASE_NAME: str = "culinary_recipes_mysql"
DATABASE_BATCH_SIZE: int = 1000
