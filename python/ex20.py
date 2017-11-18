# Ex20. Functions and files

# a program using functions to work on files

from sys import argv

script, input_file = argv

# define few functions
# def, function name, (function arguments), COLON!!!
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end= '')

# now a variable to store file contents
current_file = open(input_file)

print("First, let's print the whole file:")

# call a function on the file which content is stored in a variable
print_all(current_file)

print("Now, lets rewind the file, kind of like a tape.")

# now, call rewind function on the file, so read position is back at the beginning (0-byte)
rewind(current_file)

print("Let's print 3 lines:")

# assign a value to a variable, that will be displayed before the line's content
current_line = 1
# now call a function using the variable and .readline() command, which reads only one line from read position.
print_a_line(current_line, current_file)

current_line += 1
# '+=' is used when we wwant to increment left side with right side and assign the result to the left side as it's new values
# essentially, it is equivalent to "current_line = current_line + 1"
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
