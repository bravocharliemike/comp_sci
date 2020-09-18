"""
Chapter 5: Algorithm workbench 2
Write a program that opens the things.txt file that was created by the program
in problem 1, reads all of the data from the file before closing it, and then
displays the data from the file
"""

filename = 'things.txt'

with open(filename) as fin:
    data = fin.read()

print(data)
