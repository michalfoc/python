# Ex5 MORE VARABLES AND PRINTING

# Program using variables and printing, implementing format string using 'f'

#declaring variables
my_name = 'Michal Foc'
my_age = 30
my_height = 175 # cm
my_weight = 235 # lbs
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'brown'

print(f"Let's talk about {my_name}.")
print(f"He is {my_height} cm tall.")
print(f"He's {my_weight} lbs heavy.")
print("Actually, that is not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")


total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")
