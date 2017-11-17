# Ex17 MORE FILES

# Script copying specified files from to

# import new function 'exists' from new module 'os.path'
from sys import argv
from os.path import exists # new module and function

script, from_file, to_file = argv

print(f"Copying form {from_file} to {to_file}.")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.") # reads file's lenght 'len()'

print(f"Does the output file exist? {exists(to_file)}?") # checks if file exists 'exists()'
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w') # creates the output file with 'write' attribute
out_file.write(indata) # writes fetched data from file

print("Alright, all done.")

# remember to close all files when finished
out_file.close()
in_file.close()
