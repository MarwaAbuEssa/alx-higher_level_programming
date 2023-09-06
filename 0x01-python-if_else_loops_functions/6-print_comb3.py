#!/usr/bin/python3
for n in range(0, 10):
    for m in range(n + 1, 10):
        if n == 8 and m == 9:
            print("{0}{1}".format(n, m))
        else:
            print("{0}{1}".format(n, m), end=", ")
