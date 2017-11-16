# Ex14 PROMPTING AND PASSING

# A script using 'argv' and 'input together'.

# import argv from sys module
from sys import argv

script, user_name = argv
prompt = '>' # asign a value to the variable

print(f"Hi {user_name}, I'm the {script} script.") # prints a string using 'f-string' command including arguments from command line
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) # prompts for input and displays value of a variable in parenthesis

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And You have a {computer} computer. Nice.
""")
