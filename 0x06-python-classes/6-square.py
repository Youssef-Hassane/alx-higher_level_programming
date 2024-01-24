#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
	"""Class that defines a square by its size with various methods."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with a given size and position.

        Args:
            size (int): The size of the square, which must
            be a non-negative integer.
            position (tuple): The position of the square as a
            tuple of 2 non-negative integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, which must be a non-negative integer.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, which must be a
        tuple of 2 positive integers.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character
        to the console, offset by its position."""
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
