# Ex13 PARAMETERS, UNPACKING, VARIABLES

# A program (script) that accepts arguments from command line

# import stuff from modules
from sys import argv
script, first, second, third = argv

print("The script is called:", script) # prints a string and name of the script (program)
print("The first variable is:", first) # prints a string and value of first argument from command line
print("The second variable is:", second) # prints a string and value of second argument from command line
print("The third variable is:", third) # prints a string and value of third argument from command line
