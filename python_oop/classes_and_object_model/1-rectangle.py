#!/usr/bin/env python3
"""Este es un módulo que define la clase Rectangle."""


class Rectangle:

    """Representa un rectangulo."""
    def __init__(self, width=0, heigth=0):
        """Inicializa un nuevo rectangulo.

        Args:
            width (int): El ancho del nuevo rectangulo.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho de un rectángulo"""
        return self.__width
        
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Obtiene la altura de un rectángulo"""
        return self.__height    
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
