#!/usr/bin/python3
""" Square class """


class Square:
    """  class Square that defines a square """

    def __init__(self, size=0):
        """ Init square object

        Args:
            size (int): size of a square is crucial for a square
        """
        self.__size = size

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

    def area(self):
        """  returns the current square area """
        return (self.__size * self.__size)

    def my_print(self):
        """ prints in stdout the square with the character # """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
