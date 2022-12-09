#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            i = i.swapcase()
        else:
            i = i
        print("{}".format(i), end="")
    print("{}".format(""))
