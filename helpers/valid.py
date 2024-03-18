# valid.py
import os

def is_valid_name(name):
    """
    Check if the given name is a valid file/folder name.

    Args:
        name (str): The name to be checked.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    invalid_chars = '\\/:*?"<>|'  # Invalid characters for file/folder names on Windows OS
    return all(char not in invalid_chars for char in name)

def is_valid_path(path, name):
    """
    Check if the provided path matches the given name.

    Args:
        path (str): The path to be checked.
        name (str): The name to compare with.

    Returns:
        bool: True if the path matches the name, False otherwise.
    """
    basename = os.path.basename(path)
    return basename == name
