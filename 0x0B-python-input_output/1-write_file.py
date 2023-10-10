#!/usr/bin/python3
""" file write function."""


def write_file(filename="", text=""):
    """ writie string to a UTF8 text file

    Args:
        filename (str): file name
        text (str): text which will be writed
    Returns:
        chars count
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)
