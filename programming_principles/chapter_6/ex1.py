"""
Chapter 6: Exercise 1 File Display
Assume a file containing a series of integers is names numbers.txt and exists
on the computer's disk. Write a program that displays all of the numbers
in the file
"""

def main():
    filename = 'numbers.txt'

    fin = open(filename, 'r')

    for line in fin:
        # convert line to int
        num = int(line)
        print(num)

    fin.close()

if __name__ == '__main__':
    main()
