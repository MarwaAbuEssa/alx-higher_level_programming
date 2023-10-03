#!/usr/bin/python3
""" integer addition """


def add_integer(a, b=98):
    """ a+b 
    Float arguments are typecasted

    Raises:
        TypeError: If either of a or b is negative
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
