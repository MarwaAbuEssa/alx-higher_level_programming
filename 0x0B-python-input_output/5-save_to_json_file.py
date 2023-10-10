#!/usr/bin/python3
""" JSON file write  """
import json


def save_to_json_file(my_obj, filename):
    """ object to a text file using JSON """

    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)
