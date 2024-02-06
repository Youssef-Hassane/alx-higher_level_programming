#!/usr/bin/python3
"""
Write a class Square that inherits
from Rectangle (9-rectangle.py):
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
