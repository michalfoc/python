# 1. Study drill from Ex33




def buildlist(num):
    num = int(num)
    i = 0
    numList = []
    while i < num:
        numList.append(i)
        i += 1
        print("i: ", i)
        print("list: ", numList)

answer = int(input(">"))
buildlist(answer)
