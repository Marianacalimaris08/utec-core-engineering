#!/usr/bin/python3
"""Módulo que define la clase Square."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square hereda de Rectangle."""

    def __init__(self, size):
        """Inicializa el cuadrado validando size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Devuelve [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
        
