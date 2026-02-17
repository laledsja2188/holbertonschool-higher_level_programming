#!/usr/bin/python3
"""
This module contains a function for text indentation.
It adds 2 new lines after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The text to print with indentation

    Raises:
        TypeError: If text is not a string

    Prints:
        Text with 2 new lines after '.', '?' and ':'
        No spaces at the beginning or end of each line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""

    for char in text:
        current_line += char
        if char in ".?:":
            print(current_line.strip())
            print()
            current_line = ""

    if current_line.strip():
        print(current_line.strip())
