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
    self.integer_validator("size", size)
    super().__init__(size, size)
    self.__size = size

def area(self):
    """ return area of square """
    return self.__size * self.__size
