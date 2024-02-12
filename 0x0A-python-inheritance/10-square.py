#!/usr/bin/python3
"""
This module contain Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """initialization"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the rectangle area"""
        return self.__size*self.__size

    def __str__(self):
        """object string representation"""
        return f"[Rectangle] {self.__size}/{self.__size}"
