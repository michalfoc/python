def while_loop(number, increment):

    i = 0
    numbers = []

    while i < number:
        print(f"At the top i is %d" % i)
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is %d" % i)


    print("The numbers: ")


    for num in numbers:
        print(num)

while_loop(int(input("Enter a number: ")), int(input("Enter increment: ")))
