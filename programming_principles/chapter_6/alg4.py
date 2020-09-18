"""
Chapter 5: Algorithm workbench 4
Write code that does the following: opens 'number_list.txt' file that was
created by the code from the previous question, reads all the numbers from
the file and displays them, then closes the file
"""

filename = 'number_list.txt'

with open(filename) as fin:
    data = fin.read()

print(data)
