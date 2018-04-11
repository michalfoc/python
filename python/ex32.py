# Ex. 32 LOOPS AND LISTS

# Program building lists using for-loops

# declare some variables

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for loop goues through a lists
for number in the_count:
    print(f"This is the count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruits}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start a new none
elements = []

# then use the range to do 0 to 5 count
for i in range (0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them too
for i in elements:
    print(f"Element was: {i}")
