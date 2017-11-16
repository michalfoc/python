# Ex15. READING FILES

# script reading a file and printing its contents

# import 'argv' from 'sys' module
from sys import argv

script, filename = argv
txt = open(filename) # 'open' opens the specified file to 'prepare' it for executing other commands, i.e reading, writing etc.

print(f"Here's Your file {filename}:")
print(txt.read()) # 'read' is a function that reads the file

print("Type the filename again: ")
file_again = input("> ") # assigns a file name to a variable, which can be later called by the script

txt_again = open(file_again) # opens the file inputed by user ready for other functions

print(txt_again.read()) # clls a 'read' function on the file specified by user
