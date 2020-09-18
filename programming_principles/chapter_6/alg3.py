"""
Chapter 5: Algorithm workbench 3
Write code that does the following: opens an output file with the name
number_list.txt, uses a loop to write the numbers 1 through 100 to the file
then closes the file
"""

filename = 'number_list.txt'

with open(filename, 'w') as fout:
    for i in range(101):
        fout.write(str(i) + '\n')


