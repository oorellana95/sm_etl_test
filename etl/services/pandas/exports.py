"""
Exports functions - Pandas module
The functions are all meant to export data.
"""
import os
from datetime import datetime

from etl.config import config
from etl.services.logger import Logger


def handle_dataframe_missing_mandatory_values(df, prefix_filename):
    """Handle recipes_file with missing mandatory values"""
    df_with_nan = df[df.isna().any(axis=1)]
    invalid_recipes_count = len(df_with_nan)
    if invalid_recipes_count:
        file_path = save_dataframe_to_timestamped_csv(
            df=df_with_nan,
            filename_prefix=f"{invalid_recipes_count}_{prefix_filename}_missing_mandatory_values",
        )
        Logger.warning(
            message=f"A total of {invalid_recipes_count} recipes_file missing mandatory values have been added to {file_path} for further analysis."
        )
        return file_path


def save_dataframe_to_timestamped_csv(df, filename_prefix="data"):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{filename_prefix}.csv"
    file_path = os.path.join(config.files_config["ERROR_OUTPUT_DIR_PATH"], filename)
    df.to_csv(file_path, index=False)
    return file_path
