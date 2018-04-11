# calculator

def main():
    """main function where we input our numbers to work on and choose what operation we want to perform"""
    while True:
        x = first_number()
        while True:
            choose = input('> ')
            if choose != 'end' and choose != 'c' and choose != '+' and choose != '-' and choose != '*' and choose != '/':
                print("Not a valid operator! Try Again!")
                break
            elif choose == 'end':
                exit(0)
            elif choose == 'c':
                main()
            y = second_number()
            result = choice(choose, x, y)
            """A loop that lets us keep result of previous operation and continue working with it,
            clear the figure and start from 0,
            end the program"""
            while True:
                x = result
                while True:
                    choose = input('> ')
                    if choose != 'end' and choose != 'c' and choose != '+' and choose != '-' and choose != '*' and choose != '/':
                        print("Not a valid operator! Try Again!")
                        break
                    elif choose == 'end':
                        exit(0)
                    elif choose == 'c':
                        main()
                    y = second_number()
                    result = choice(choose, x, y)

def add(a, b):
    """simple function performing addition"""
    a += b
    return a

def subtract(a, b):
    """simple function performing subtraction"""
    a -= b
    return a

def multiply(a, b):
    """simple function performing multiplication"""
    a *= b
    return a

def divide(a, b):
    """simple function performing division"""
    a /= b
    return a

def choice(arg1, arg2, arg3):
    """function allowing us to choose the operation to be performed on numbers that we provide in main() function"""
    a = arg2
    b = arg3
    x = arg1
    if x == '+':
        x = add(a, b)
    elif x == '-':
        x = subtract(a, b)
    elif x == '*':
        x = multiply(a, b)
    elif x == '/':
        x = divide(a, b)
    else:
        print('Again!')
        main()
    print(x)
    return x

def first_number():
    """function testing first input if it is a number"""
    x = 0
    print(x)

    while True:
        try:
            x = float(input())
            break
        except ValueError:
            print('Try again!')

    return x

def second_number():
    """function testing second input if it is a number"""
    x = 0

    while True:
        try:
            x = float(input())
            break
        except ValueError:
            print('Try again!')

    return x

main()
