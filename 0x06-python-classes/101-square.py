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

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """ edfine print for square """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
