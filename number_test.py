import random
import math
import statistics


def random_list(qty, small, big):
    """Generates a random list of quantity integers between minimum and maximum (inclusive)
    """
    return [random.randint(small, big) for number in range(qty)]


# Beginning of the program
print('Welcome to the Number List Test program')

# Getting the user to select difficulty of the test
while True:
    level = input('Select a difficulty:\n'
                  '[E]asy\n'
                  '[M]edium\n'
                  '[H]ard\n'
                  '> ').upper()     # Convert user input to all UPPERCASE
    if level == 'E':
        print('Easy difficulty selected!\n')
        questions = 2
        quantity = 3
        minimum, maximum = 1, 5
        break
    elif level == 'M':
        print('Medium difficulty selected!\n')
        questions = 4
        quantity = 5
        minimum, maximum = 3, 12
        break
    elif level == 'H':
        print('Hard difficulty selected!\n')
        questions = 6
        quantity = 8
        minimum, maximum = 10, 25
        break
    else:
        print('Invalid choice! Enter E, M or H.')

# Initialise variable to keep track of the user's correct answers
score = 0

for i in range(questions):
    # User is up to last question so this is Challenge Question
    if i + 1 == len(range(questions)):
        print(f'Question {i + 1} of {questions}.')
        print('Challenge Question!')
        number_list = random_list(quantity, minimum * 2, maximum * 2)

    # User is not up to last question
    else:   # i + 1 < len(range(questions)):
        print(f'Question {i + 1} of {questions}.')
        number_list = random_list(quantity, minimum, maximum)

    # Randomly show the user different types of questions
    question_type = random.randint(1, 4)
    if question_type == 1:
        answer = int(input(f'What is the smallest number in this list? {number_list}\n'
                           '> '))
        if answer == min(number_list):
            print('Correct!\n')
            score += 1
        else:
            print(f'Incorrect! Correct answer was {min(number_list)}\n')

    elif question_type == 2:
        answer = int(input(f'What is the biggest number in this list? {number_list}\n'
                           '> '))
        if answer == max(number_list):
            print('Correct!\n')
            score += 1
        else:
            print(f'Incorrect! Correct answer was {max(number_list)}\n')

    elif question_type == 3:
        answer = int(input(f'What is the sum of the numbers in this list? {number_list}\n'
                           '> '))
        if answer == sum(number_list):
            print('Correct!\n')
            score += 1
        else:
            print(f'Incorrect! Correct answer was {sum(number_list)}\n')

    elif question_type == 4:
        answer = int(input(f'What is the average of the numbers in this list? {number_list}\n'
                           '(round UP to nearest integer)\n'
                           '> '))
        average = statistics.mean(number_list)  # Calculate the average of the numbers in random list
        if answer == math.ceil(average):        # Rounds up the average to the nearest integer
            print('Correct!\n')
            score += 1
        else:
            print(f'Incorrect! Correct answer was {math.ceil(average)}\n')

# Test is complete and the user can see their score
print('Test Complete!')
print(f'You scored {score}/{questions} ({score/questions * 100}%)')