#!/usr/bin/python3
""" Square class """


class Square:
    """  class Square that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Init square object

        Args:
            size (int): size of a square is crucial for a square
            position (int, int): typle position for square
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """ size getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ size setter """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ getter for position """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """  returns the current square area """
        return (self.__size * self.__size)

    def __eq__(self, second):
        """ == """
        return self.area() == second.area()

    def __ne__(self, second):
        """ != """
        return self.area() != second.area()

    def __lt__(self, second):
        """ less than or equal """
        return self.area() <= second.area()

    def __gt__(self, second):
        """ greater than  """
        return self.area() > second.area()

    def __ge__(self, second):
        """ greater than or equal """
        return self.area() >= second.area()
