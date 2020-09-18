"""
Chapter 6: Exercise 2 - File Head Display
Write a program that asks the user for the name of a file. The program
should display only the first five lines of the file's contents. If the file
contains less than five lines, it should display the file's entire contents.
"""

def main():
    # Ask user for the name of a file and save it into filename
    filename = input('Enter the name of the file: ')

    # Open the file in read mode
    fin = open(filename, 'r')
    line = fin.readline()
    counter = 1

    while line != '' and counter <= 5:
        num = line
        print(num.strip('\n'))
        counter += 1
        
        # Read the next line
        line = fin.readline()

    fin.close()

if __name__ == '__main__':
    main()
