# Ex. 29 WHAT IF

# Program using if-statement

# declare some variables to test:
people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled in!")

if people > dogs:
    print("The world is dry!")

# change one of the variables:
dogs += 5 # or dogs = dogs + 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
