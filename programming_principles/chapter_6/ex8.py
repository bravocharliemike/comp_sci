"""
Chapter 6: Exercise 8 - Word List File Writer
Read the words from a file and display the following data:
    * Number of words in file
    * Longest word in the file
    * Average length of all the words in the file
"""

def report_results(words, longest, average):
    print(f'Total number of words:\t{str(words)}')
    print(f'Longest word:\t{longest}')
    print(f'Average word length:\t{str(average)}')

def main():

    filename = 'words.txt'
    longest_word = ''
    total_length = 0
    total_words = 0

    fin = open(filename)
    
    for word in fin:
        word = word.rstrip('\n')
        word_length = len(word)

        total_length += word_length
        total_words += 1

        # Check for longest word
        if word_length > len(longest_word):
            longest_word = word
    
    fin.close()
    # Determine average length
    average = total_length / total_words 

    # Report the data
    report_results(total_words, longest_word, average)

if __name__ == '__main__':
    main()
