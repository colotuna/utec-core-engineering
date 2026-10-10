#!/usr/bin/env python3

for letra in "abcdefghijklmnopqrstuvwxyz":
    if letra == 'q' or letra == 'e':
        continue
    print("{:s}".format(letra), end="")
