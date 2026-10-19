#!/usr/bin/env python3

from calculator_1 import add, sub, multiplication, division

if __name__ == "__main__":

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, multiplication(a, b)))
    print("{} / {} = {}".format(a, b, division(a, b)))
