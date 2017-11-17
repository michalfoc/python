# Ex19.1

from sys import argv

script, name_file, last_name_file, main_name, secondary_name = argv

def credentials(name, last_name):
    print(f"My name... is {name} {last_name}!!! Don't f*** with me !!")


# 1. use files
name_data = open(name_file).read()
last_name_data = open(last_name_file).read()

credentials(name_data, last_name_data)

# 2. use direct method
credentials("Tony", "Montana")

#3. using variables
first, last = "Tony", "Montana"
credentials(first, last)

#4. using math
credentials("T" + "o" + "n" + "y", "M" + "o" + "n" + "t" + "a" + "n" + "a")

#5. using f-string
first_name = '{}'
surname = '{}'
credentials(first_name.format("Tony"), surname.format("Montana"))

#6. using user input
credentials(input(), input())

#7. combination of f-string and variables
credentials(first_name.format("Tony"), last)

#8. combination of math, f-string and input
credentials("T" + "o" + "n" + "y", surname.format(input()))

#9. use files (different method)
f1 = open('ex19.1.1.longer_file.txt')
lines1 = f1.readlines()
x = lines1[2]
f2 = open('ex19.1.2.longer_file.txt')
lines2 = f2.readlines()
y = lines2[7]
credentials(x,y)

#10. using arguments 'argv'
credentials(main_name, secondary_name)
