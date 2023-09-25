#!/usr/bin/python3
real_number = 0
for i in range(x):
    try:
        print("{}".format(my_list[i]), end="")
        real_number +=1
    except IndexError:
        print("Index exception")
        break
    print("")
    return (real_number)
