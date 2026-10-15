#!/usr/bin/env python3

def pow(a, b):
    if b == 0:
        result = 1

    result = 1
    is_negative = b < 0
    b = abs(b)

    for _ in range(b):
        result *= a

    if is_negative:
        return 1 / result

    return result
