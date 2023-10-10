#!/usr/bin/python3
""" subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a square."""

def __init__(self, size):
    """Initialize a new square.

    Args:
        size (int): the size of new square
    """
    super().__init__(self.__size, self.__size)
    self.integer_validator("size", size)
    self.__size = size

def area(self):
    """area"""

    return self.__size * self.__size
