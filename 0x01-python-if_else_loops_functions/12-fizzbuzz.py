#!/usr/bin/python3
def fizzbuzz():
    for i in range(101):
        if i % 15 == 0:
            i = "FizzBuzz"
        if i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
        else:
            i = i
        print("{}".format(i), end=" ")