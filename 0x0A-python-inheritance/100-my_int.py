#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

     def __ne__(self, value):
         """Override != operator with == behavior."""
         return self.real == value
