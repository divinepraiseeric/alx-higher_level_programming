#!/usr/bin/python3
def print_last_digit(number):
    print("{}".format(abs(int(number)) % 10), end="")
    return abs(int(number)) % 10
