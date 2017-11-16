# Ex15. READING FILES

# script reading a file and printing its contents
# using 'argv' only

# import 'argv' from 'sys' module
from sys import argv

script, filename = argv
txt = open(filename) # 'open' opens the specified file to 'prepare' it for executing other commands, i.e reading, writing etc.

print(f"Here's Your file {filename}:")
print(txt.read()) # 'read' is a function that reads the file
