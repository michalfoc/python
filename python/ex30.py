# Ex.30

# program expanding if-statement with elif and else

# declare some variables for testing
people = 30
cars = 40
trucks = 15

# ... and test them
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take trucks.")
else:
    print("Fine, let's just stay home.")
