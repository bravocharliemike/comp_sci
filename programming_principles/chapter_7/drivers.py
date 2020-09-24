ANSWERS = [
        'A', 'C', 'A', 'A', 'D',
        'B', 'C', 'A', 'C', 'B',
        'A', 'D', 'C', 'A', 'D', 
        'C', 'B', 'B', 'D', 'A',
    ]


def main():
    # define needed variables
    total_correct = 0
    wrong_questions = []
    
    try:
        # Open the user file with their answers
        filename = 'answers.txt'
        with open(filename, 'r') as fin:
            answers = fin.read().split()    # creating a list of strings with answers

        # Compare the user answers with the correct ones
        for index, i in enumerate(zip(answers, ANSWERS)):
            if i[0] == i[1]:
                total_correct +=1
            else:
                # add question number of incorrectly answered question
                wrong_questions.append(index + 1)
        
        # print a message if student passes (15/20 right)
        if total_correct >= 15:
            print('You have passed the exam!')
        else:
            print('You have failed the exam.')

        # inform user how many answers they got right
        print(f'You answered {total_correct} questions correctly.')

        # inform user how many they got incorrect
        print(f'You got {20 - total_correct} questions wrong.')

        # provide question numbers of incorrect answers
        if not len(wrong_questions):
            print('You got a perfect score')
        else:
            print('You answered the following questions incorrectly')
            print(wrong_questions)
    
    # handle possible errors
    except IOError:
        print('The file could not be found')
    except IndexError:
        print('There was an indexing error')



if __name__ == '__main__':
    main()
