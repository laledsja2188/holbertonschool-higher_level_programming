#!/usr/bin/python3
"""
This module contains a function for printing names.
It handles string validation and default values.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted name string.

    Args:
        first_name (str): The first name to print
        last_name (str, optional): The last name to print. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string

    Prints:
        "My name is <first_name> <last_name>"
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
