#!/usr/bin/env python3

"""Módulo que contiene una función para leer un archivo de texto."""

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
