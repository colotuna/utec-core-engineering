#!/usr/bin/env python3
"""Este es un módulo que define la clase Square."""


class Square:

    """Representa un cuadrado."""
    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): El tamaño del nuevo cuadrado.
        """
        self.__size = size