#Ex 5.1 A BIT MORE ON VARIABLES

# Program asking a user for input and converting cm to inches and kg to punds and other way around

name = input("What is your name?\n")
age = input("How old are You?\n")
height = float(input("How tall are You?\n"))
x = input("Is that inches or centymeters?('in' for inches, 'cm' for centymeters)\n")
weight = float(input("How mcuh do you weigh?\n"))
y = input("Is that in punds or kilograms?('lbs' for pound, 'kg' for kilograms)\n")

if x == 'in' and y == 'lbs'
    height = int(height * 2.54)
    weight = int(weight / 2.2)
    print(f"So, Your name is {name}, You are {age} years old, You are {height} cm tall and {weight} kilograms heavy.")
elif x == 'cm' and y == 'kg':
    height = int(height / 2.54)
    weight = int(weight * 2.2)
    print(f"So, Your name is {name}, You are {age} years old, You are {height} in tall and {weight} pounds heavy.")
else:
    print("Use only one type of measurements (imperial or metric)!")
