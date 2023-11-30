import os


def ensure_directory_exists(directory_path: str) -> None:
    """
    Verify that the directory exists. If it does not exist, create another directory.
    :param
    - str directory_path
    :return:
    :rtype: bool
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    return
