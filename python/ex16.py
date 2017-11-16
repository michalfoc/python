#Ex16 READING AND WRITING FILES

# script teaching commands usable with files

# import 'argv' from module 'sys'
from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("if You don't want that, hit CTRL-C (^C).")
print("If You want to do that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now, I'm going to ask you for three lines.")

line1, line2, line3 = input("Line1: "), input("Line2: "), input("Line3: ")

print("I'm going to write these to the file")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finaly, we will close it.")
target.close()
