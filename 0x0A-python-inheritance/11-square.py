#!/usr/bin/python3
"""
Write a class Square that inherits from
Rectangle (9-rectangle.py)
(task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the print() and str().
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
