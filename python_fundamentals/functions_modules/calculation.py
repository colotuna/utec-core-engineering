#!/usr/bin/env python3

from calculator_1 import sumar,restar,multiplicar,dividir

if __name__ = "__main__":

    a = 10
    b = 5

    print("El resultado de a + b es = {}".format(sumar(a, b)))
    print("El resultado de a - b es = {}".format(restar(a, b)))
    print("El resultado de a * b es = {}".format(multiplicar(a, b)))
    print("El resultado de a / b es = {}".format(dividir(a, b)))
