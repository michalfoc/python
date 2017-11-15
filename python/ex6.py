# Ex6. STRINGS AND TEXT

#  Aprogram showing different ways to use strings and text

# using f-string and variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: '{x}'")
print(f"I also said: '{y}'")

# using .format (another type of formatiing, more in Ex.17.py)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

# using variables and math
w = "This is left side of..."
e = "a string with a right side."

print(w + e)
