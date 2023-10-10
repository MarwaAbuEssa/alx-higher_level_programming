#!/usr/bin/python3
"""  a class Rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """ rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """" a new Rectangle.

        Args:
            width (int): The width
            height (int): The height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
