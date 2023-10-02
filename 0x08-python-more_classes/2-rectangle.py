#!/usr/bin/python3
""" Rectangle class."""

class Rectangle:
    """ a rectangle."""
    
    def __init__(self, width=0, height=0):
        """ init rectangular 

        Args:
        width (int): The width of rectangle
        height (int): The height of  rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area of rectangular """
        return (self.__width * self.__height)

    def perimeter(self):
        """ return perimeter of rect """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

