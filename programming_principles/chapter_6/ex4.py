"""
Chapter 6: Exercise 4 - High Score
A file scores.txt exists on the computer. It contains a series of records
each with two fields: a name followed by a score. Write a program that
displays the name and score of the record with the highest score, as well as
the number of records in the file.
"""

def main():
    filename = 'scores.txt'

    fin = open(filename, 'r')
    name = fin.readline()
    high_score = 0
    high_scorer = ''
    counter = 0

    while name != '':
        counter += 1
        name = name.rstrip('\n')
        score = int(fin.readline().rstrip('\n'))
        if score > high_score:
            high_score = score
            high_scorer = name
        name = fin.readline()

    fin.close()

    print(f"High scorer: {high_scorer} with score {high_score}")
    print(f"Ther are {counter} total records")


if __name__ == '__main__':
    main()

