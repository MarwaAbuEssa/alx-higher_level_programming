#!/usr/bin/python3
""" load json from file """
import json


def load_from_json_file(filename):
    """  object from a JSON file."""
    with open(filename) as myFile:
        return json.load(myFile)
