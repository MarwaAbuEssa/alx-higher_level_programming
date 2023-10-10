#!/usr/bin/python3
""" an inherited list class MyList."""

class MyList(list):
    """ sorted printing for the built-in list class """


    def print_sorted(self):
        """Print sorted list """
        print(sorted(self))
