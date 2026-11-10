#!/usr/bin/env python3
"""Este es un módulo que define la clase Square."""


class Square:

    """Representa un cuadrado."""
    def __init__(self, size):
        """Inicializa un nuevo cuadrado."""
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        """Args:
            size (int): El tamaño del nuevo cuadrado.
        """
        self.__size = size
