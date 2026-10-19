#!/usr/bin/env python3

from calculator_1 import sumar,restar,multiplicar,dividir

if __name__ == "__main__":

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, sumar(a, b)))
    print("{} - {} = {}".format(a, b, restar(a, b)))
    print("{} * {} = {}".format(a, b, multiplicar(a, b)))
    print("{} / {} = {}".format(a, b, dividir(a, b)))
