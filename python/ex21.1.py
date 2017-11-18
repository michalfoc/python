# Ex21.1 # very simple calculator!


def add(a, b):
    print(f"ADDING {a} + {b}") # little message
    return a + b # return the result of math between two arguments, could be anything, that you place on the right hand side of = character, when declaring variables!

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

calculation = input('What You want to do? + - * /')

if calculation == '+':
    A1 = add(float(input('> ')), float(input('> ')))
    print(A1)
elif calculation == '-':
    A2 = subtract(float(input('> ')), float(input('> ')))
    print(A2)
elif calculation == '*':
    A3 = multiply(float(input('> ')), float(input('> ')))
    print(A3)
elif calculation == '/':
    A4 = divide(float(input('> ')), float(input('> ')))
    print(A4)
else:
    print("Learn to read and come back!! Moron...")
