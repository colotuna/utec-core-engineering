#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0

    for index in range(x):
        try:
            print("{:d}".format(values[index]), end="")
        except (TypeError, ValueError):
            continue

        printed += 1

    print()
    return printed
