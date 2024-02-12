#!/usr/bin/python3
"""
Write a class Square that inherits
from Rectangle (9-rectangle.py):
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square with a given size.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
