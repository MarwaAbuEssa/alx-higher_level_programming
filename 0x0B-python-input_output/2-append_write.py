#!/usr/bin/python3
""" file write function."""


def write_file(filename="", text=""):
    """ append string to a UTF8 text file

    Args:
        filename (str): file name
        text (str): text which will be appended
    Returns:
        chars count
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
