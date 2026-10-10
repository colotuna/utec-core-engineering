#!/usr/bin/env python3
resultado = ""

for letra in "abcdefghijklmnopqrstuvwxyz":
    if letra == 'q' or letra == 'e':
        continue
    resultado += letra

print(resultado)
