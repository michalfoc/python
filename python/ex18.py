# Ex18 NAMES, VARIABLES, CODE, FUNCTIONS

# Introduction to functions

# this one is like scripts with 'argv'
def print_two(*args): # def - 'define', tells python that we are making a functiíon
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}.")

# ok, that *args is actually pointless, let's just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}.")

# this one only takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}.")

# this one takes none
def print_none():
    print("I got nothing.")

print_two("Michal", "Foc")
print_two_again("Michal", "Foc")
print_one("Michal")
print_none()
