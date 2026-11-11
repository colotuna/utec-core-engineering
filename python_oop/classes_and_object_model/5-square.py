#!/usr/bin/env python3
"""Este es un módulo que define la clase Square."""


class Square:

    """Representa un cuadrado."""
    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado."""
        self.size = size

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula el área del cuadrado.

        Returns:
            int: El área del cuadrado.
        """
        return (self.__size ** 2)

    def my_print(self): 
        """Imprime el cuadrado con el caracter #.

        Si el tamaño es 0, imprime una línea en blanco.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
