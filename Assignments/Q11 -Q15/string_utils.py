# string_utils.py

def reverse_string(s):
    """
    Reverses the given string.

    Args:
    s (str): The string to reverse.

    Returns:
    str: The reversed string.
    """
    return s[::-1]

def capitalize_string(s):
    """
    Capitalizes the first letter of each word in the given string.

    Args:
    s (str): The string to capitalize.

    Returns:
    str: The capitalized string.
    """
    return s.title()

def upper_case_string(s):
    """
    Converts the given string to uppercase.

    Args:
    s (str): The string to convert to uppercase.

    Returns:
    str: The uppercase string.
    """
    return s.upper()

def lower_case_string(s):
    """
    Converts the given string to lowercase.

    Args:
    s (str): The string to convert to lowercase.

    Returns:
    str: The lowercase string.
    """
    return s.lower()

def remove_whitespace(s):
    """
    Removes leading and trailing whitespace from the given string.

    Args:
    s (str): The string to trim.

    Returns:
    str: The trimmed string.
    """
    return s.strip()
