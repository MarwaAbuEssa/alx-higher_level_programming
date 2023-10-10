#!/usr/bin/python3
""" class-checking inherits_from function."""


def inherits_from(obj, a_class):
    """ object is inherted an instance of a given class.

    Args:
        obj (any): The object
        a_class (type): The class to compare
    Returns:
        if inherted from  return true else
        return false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
