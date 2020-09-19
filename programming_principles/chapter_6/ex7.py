"""
Chapter 6: Exercise 7 - Word List File Write
Ask user how many words they would like to write to a file, and then
asks the user to enter that many words, one at a time. The words are then
written to a file
"""

def main():
    # Prepare file to write
    filename = 'words.txt'
    fout = open(filename, 'w')

    words = int(input('How many words do you wish to enter: '))
    counter = 1

    for word in range(1, words + 1):
        word = input(f'Enter word number {counter}: ')
        counter += 1
        fout.write(word + '\n')
        print(f'{word} was written to the file')

    fout.close()
    print(f'The file {filename} has been saved.')


if __name__ == '__main__':
    main()
