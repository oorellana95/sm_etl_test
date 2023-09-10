import os

import pytest

from etl.config import config


@pytest.fixture(scope="function")
def temp_dir(request):
    temp_path = config.files_config["ERROR_OUTPUT_DIR_PATH"]
    os.makedirs(temp_path)

    def fin():
        for root, dirs, files in os.walk(temp_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(temp_path)

    request.addfinalizer(fin)

    return temp_path
