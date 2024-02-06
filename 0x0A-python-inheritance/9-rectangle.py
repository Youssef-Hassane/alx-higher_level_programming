#!/usr/bin/python3
"""
Write a class Rectangle that inherits from
BaseGeometry (7-base_geometry.py)
(task based on 8-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the Rectangle with width and height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
