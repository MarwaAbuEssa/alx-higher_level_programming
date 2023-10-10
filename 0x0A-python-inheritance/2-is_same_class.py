#!/usr/bin/python3
""" class-checking function."""


def is_same_class(obj, a_class):
    """ object is exactly an instance of a given class.

    Args:
        obj (any): The object
        a_class (type): The class to compare
    Returns:
        if exact match return true else
        return false
    """
    if type(obj) == a_class:
        return True
    return False
