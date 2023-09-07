#!/usr/bin/python3
def uppercase(str):
    for cha in str:
        if ord(cha) >= 97 and ord(cha) <= 122:
            cha = chr(ord(cha) - 32)
         print("{0}".format(cha), end="")
    print("")
