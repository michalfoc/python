# Ex15. READING FILES

# script reading a file and printing its contents
# using input only

print("Type the filename again: ")
file_again = input("> ") # assigns a file name to a variable, which can be later called by the script

txt_again = open(file_again) # opens the file inputed by user ready for other functions

print(txt_again.read()) # clls a 'read' function on the file specified by user
