"""
Chapter 5: Algorithm workbench 1
Write a program that opens an output file with the name things.txt, writes
the name of an animal, a fruit and a country to the file on separate lines
then closes the file
"""

filename = 'things.txt'

words = [
        'dog',
        'banana',
        'Australia'
        ]

with open(filename, 'w') as fout:
    for word in words:
        fout.write(word + '\n')


