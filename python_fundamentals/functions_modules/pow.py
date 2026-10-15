#!/usr/bin/env python3

def pow(a, b):
    result = 1
    a = abs(a)
    b = abs(b)

    for _ in range(b):
        result *= a

    return result
