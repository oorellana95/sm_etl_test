"""
Exports functions - Pandas module
The functions are all meant to export data.
"""
import os
from datetime import datetime

from etl.config import PATH_OUTPUT_DIR


def save_dataframe_to_timestamped_csv(df, filename_prefix="data"):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{filename_prefix}.csv"
    file_path = os.path.join(PATH_OUTPUT_DIR, filename)
    df.to_csv(file_path, index=False)
    return file_path
