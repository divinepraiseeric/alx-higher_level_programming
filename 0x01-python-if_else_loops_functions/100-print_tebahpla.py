#!/usr/bin/python3
# A - Z, 65 - 90.  a - z, 97 -122
for i in range(97, 123):
    # if I is odd than small case, if i is even then uppercase
    if (i % 2 == 0):
        i = chr(219 - i - 32)
        # 219 - i ensures nth-to-the-last instead of nth
        # as in (backwards/reverse printing)
        # further subtracting 32 takes the chr to uppercase.
    else:
        i = chr(219 - i)
    print("{}".format(i), end="")
