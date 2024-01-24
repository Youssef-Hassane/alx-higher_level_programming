#!/usr/bin/python3
"""defines a square"""


class Square:

    """Class that defines a square by its size with various methods."""
    def __init__(self, size=0):
        """Initialize a new Square with a given size.

        Args:
            size (int): The size of the square,
            which must be a non-negative integer.
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: The current size of the square.
        """
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

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character.

        If the size of the square is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
