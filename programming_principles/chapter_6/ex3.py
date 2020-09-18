"""
Chapter 6: Exercise 3 - Line Numbers
Write a program that asks the user for the name of a file. The program should
display the contents of the file with each line preceded with a line number
followed by a colon. The line numbering should start at 1.
"""

def main():
    filename = input('Enter the name of the file: ')

    fin = open(filename, 'r')
    contents = fin.readlines()

    for idx, line in enumerate(contents, 1):
        l = str(idx) + ': ' + str(line)
        print(l.rstrip('\n'))

    fin.close()


if __name__ == '__main__':
    main()
