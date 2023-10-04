#!/usr/bin/python3
"""a square-printing"""

def print_square(size):
    """a square with the # character.

    Args:
        size (int): height/width.
    Raises:
        TypeError: size is not an integer
        ValueError: size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
