#!/usr/bin/python3
""" a text file-reading function."""


def read_file(filename=""):
    """ contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
