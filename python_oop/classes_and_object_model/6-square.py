#!/usr/bin/env python3
"""Module that defines a class Square with size, position and str."""


class Square:
    """Class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a validated size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        print(str(self))

    def __str__(self):
        """Return the square as a string."""
        if self.__size == 0:
            return ""
        row = " " * self.__position[0] + "#" * self.__size
        lines = [""] * self.__position[1] + [row] * self.__size
        return "\n".join(lines)
