# Ex21. FUNCTIONS CAN RETURN SOMETHING

# A pgrogram, where functions 'return' stuff

# def function_name (function_arguments, ...) : <- COLON!!!
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


print("Let's do some math with just functions!")

# declaring variables and calling functions to assign results to said variables
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 3)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}.")

# A puzzle:

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes : ", what, "Can you do it by hand?")
