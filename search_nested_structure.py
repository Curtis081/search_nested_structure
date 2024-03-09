from typing import List, Tuple, Union


def search_nested_structure(data: Union[Tuple, List, dict, int, str, float, bool], target: str) -> bool:
    """
    Recursively search a nested structure for a specific target string.

    Parameters:
    - data: The nested structure (tuple, list, dictionary) to search.
    - target: The string to search for.

    Returns:
    - True if the target string is found, False otherwise.
    """
    if isinstance(data, (Tuple, List)):
        # If data is a tuple or list, iterate through its elements
        for item in data:
            if search_nested_structure(item, target):
                return True
    elif isinstance(data, dict):
        # If data is a dictionary, iterate through its values
        for value in data.values():
            if search_nested_structure(value, target):
                return True
    elif isinstance(data, Union[int, str, float, bool]):
        # If data is a string, compare with the target
        if data == target:
            return True

    # If the target is not found in the current structure
    return False
