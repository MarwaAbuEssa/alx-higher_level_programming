#!/usr/bin/python3
""" a rectangle class."""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ a new Rectangle.

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
            x (int): Rectangle x coordinate
            y (int): Rectangle y coordinate
            id (int): Rectangle id
        Raises:
            TypeError: width or height is not an int
            TypeError: x or y is not an int
            ValueError: width or height <= 0
            ValueError: x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the Rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set get the height of the Rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """ Set get the x coordinate of the Rectangle."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ the area of the Rectangle."""
        return self.width * self.height

        def display(self):
            """ the Rectangle using the `#` character."""
            if self.width == 0 or self.height == 0:
                print("")
                return
            [print("") for y in range(self.y)]
            for h in range(self.height):
                [print(" ", end="") for x in range(self.x)]
                [print("#", end="") for w in range(self.width)]
                print("")

        def update(self, *args, **kwargs):
            """Update the Rectangle

            Args:
            *args (ints): New attribute values
                1- id attribute
                2- width attribute
                3- height attribute
                4- x attribute
                5- y attribute
            **kwargs (dict): New key/value pairs of attributes
            """
            if args and len(args) != 0:
                a = 0
                for arg in args:
                    if a == 0:
                        if arg is None:
                            self.__init__(self.width, self.height,
                                          self.x, self.y)
                        else:
                            self.id = arg
                    elif a == 1:
                        self.width = arg
                    elif a == 2:
                        self.height = arg
                    elif a == 3:
                        self.x = arg
                    elif a == 4:
                        self.y = arg
                    a += 1
            elif kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        if v is None:
                            self.__init__(self.width, self.height,
                                          self.x, self.y)
                        else:
                            self.id = v
                    elif k == "width":
                        self.width = v
                    elif k == "height":
                        self.height = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

        def to_dictionary(self):
            """ dictionary representation of a Rectangle."""
            return {"id": self.id, "width": self.width,
                    "height": self.height, "x": self.x,
                    "y": self.y}

        def __str__(self):
            """ print() and str() representation of the Rectangle."""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                           self.x, self.y,
                                                           self.width,
                                                           self.height)
