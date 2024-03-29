#!/usr/bin/python3
""" This is the "Rectangle"  module """


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the Rectangle with the '#' character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rows = []
        for i in range(self.__height):
            rows.append(str(self.print_symbol) * self.__width)
        return "\n".join(rows)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({self.width}, {self.height})".format(self=self)

    def __del__(self):
        """Print a message for deletion of a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
