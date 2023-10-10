#!/usr/bin/python3
""" a base geometry class BaseGeometry."""


class BaseGeometry:
    """ base geometry."""

    def area(self):
        """ no implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ parameter as an integer.

        Args:
            name (str): The name
            value (int): The parameter
        Raises:
            TypeError: If value is not an int
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
