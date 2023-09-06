import os

# Critical values should be as SECRETS.

# General
PROJECT_NAME: str = "sm_etl_test"
SERVICE_NAME: str = "ETL Service"

# Files
PATH_ROOT_DIR = os.path.abspath("")
PATH_INPUT_DIR = os.path.join(PATH_ROOT_DIR, "data_test")
RAW_USERS_PATH = os.path.join(PATH_INPUT_DIR, "RAW_users.csv")
RAW_RECIPES_PATH = os.path.join(PATH_INPUT_DIR, "RAW_recipes.csv")
RAW_INTERACTIONS_PATH = os.path.join(PATH_INPUT_DIR, "RAW_interactions.csv")

# Database
DATABASE_DIALECT: str = "mysql+pymysql"
DATABASE_HOST: str = "localhost"
DATABASE_PORT: int = 3306
DATABASE_USER: str = "master"
DATABASE_PASSWORD: str = "pass"
DATABASE_NAME: str = "culinary_recipes_mysql"
