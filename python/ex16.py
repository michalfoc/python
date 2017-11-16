#Ex16 READING AND WRITING FILES

# script teaching commands usable with files

# import 'argv' from module 'sys'
from sys import argv

script, filename = argv # usuall arguments for command line, if You want a file in different location need to give full path for it.

print(f"We are going to erase {filename}.") #  prints a string with f-string function
print("if You don't want that, hit CTRL-C (^C).")
print("If You want to do that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # 'open' opens the file in "write" mode ('w') and assigns it to variable

print("Truncating the file.  Goodbye!")
target.truncate() # Truncates (erases) the content of the file

print("Now, I'm going to ask you for three lines.")

line1, line2, line3 = input("Line1: "), input("Line2: "), input("Line3: ") # declaring some variables as strings

print("I'm going to write these to the file")

# we write the input from user into a file
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finaly, we will close it.")
target.close() # file should be closed after we finish using it.
