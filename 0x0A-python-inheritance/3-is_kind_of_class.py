#!/usr/bin/python3
""" class-checking function."""


def is_kind_of_class(obj, a_class):
    """ object object is an instance of a given class.

    Args:
        obj (any): The object
        a_class (type): The class to check the type
    Returns:
        if exact match return true else
        return false
    """
    if isinstance(obj, a_class):
        return True
    return False
