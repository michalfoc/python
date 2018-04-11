# 1. Study drill from Ex33


# function building a list

def build_list(num):
    num = int(num)
    i = 0
    numList = []
    while i < num:
        print("i: ", i)
        numList.append(i)
        i += increment
        print("list: ", numList)

list_range = int(input("Range of numbers to be inserted into a list:\n>"))
increment = float(input("Increment of numbers in the list:\n>"))

build_list(list_range)
