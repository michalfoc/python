# Ex 8 PRINTING, PRINTING

# More of f-string and more complicated uses of it.

#declare Your variable
formatter = "{} {} {} {}" # "{}" are used to take new values with use of .format command

print(formatter.format(1, 2, 3, 4)) # replaces {} with respective values
print(formatter.format("one", "two", "three", "four")) # as above, instead of numbers, used strings
print(formatter.format(formatter, formatter, formatter, formatter)) # in this case we use variable's value itself to insert
print(formatter.format(
    "Try Your",
    "Own text here.",
    "Maybe a poem",
    "Or a song about fear." # this is how You use multiple lines of code to be displayed on a single line
))
print(formatter.format("Try Your", "\nOwn text here", "\nMaybe a poem,", "\nOr a song about fear.")) # and this is how you create single line of code to be displayed on multiple lines
