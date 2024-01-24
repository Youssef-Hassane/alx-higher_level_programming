#!/usr/bin/python3
"""Access and update private attribute"""


class Square:

    """Access and update private attribute"""
    def __init__(self, size=0):
        self.__size = size

    """Access and update private attribute"""
    @property
    def size(self):
        return self.__size

    """Access and update private attribute"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Access and update private attribute"""
    def area(self):
        return self.__size ** 2
