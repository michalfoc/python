# project
import os

def create_file(f):
    """opens the file with amend, writes defined data to it and closes it at the end"""
    new_file = open(f, 'a')
    new_file.write(indata)
    new_file.close()

file_name = (input('filename: ') + '.txt')
indata = ('ITEM \tQUANTITY\n')
create_file(file_name)
i = 0

while i < 1:
    indata = (input('ITEM: ') + ' \t' + input('QUANTITY: ') + '\n')
    create_file(file_name)
    if indata == ' \t\n':
        file_again = input('Input filename for printing: ')
        os.startfile(file_again, "print") # imported from os, easy print command
        exit(0)
    continue
