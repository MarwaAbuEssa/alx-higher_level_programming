#!/usr/bin/python3
""" function that adds attributes to objects """


def add_attribute(obj, att, value):
    """  new attribute to an object
    Args:
        obj (any): The object to add
        att (str): The name of the attribute
        value (any): The value of att
    Raises:
        TypeError: If the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
