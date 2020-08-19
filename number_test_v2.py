"""
Assignment 1: Number List Test Program
Student: Bernardo CAMEJO
Student number: 10528885
Version 2.0
Date: 19/08/2020

This program will generate a "Number List Test" that creates lists of random
integers and asks the user different random questions about them. The program
allows the user to select the difficulty of the test, which determines the
number of questions in the test, as well as the quantity and range of the
randomly generated numbers.
"""
import random
import math
import statistics


def random_list(quantity: int, minimum: int, maximum: int) -> list:
    """Generates a random list of quantity integers between minimum
    and maximum (inclusive)"""
    return [random.randint(minimum, maximum) for number in range(quantity)]


# Start of the program
print('Welcome to the Number List Test program')

# User chooses the difficulty of the test
# Variables are set according to the difficulty level
while True:
    level = input('Select a difficulty:\n'
                  '[E]asy\n'
                  '[M]edium\n'
                  '[H]ard\n'
                  '> ').upper()     # Convert user input to all UPPERCASE
    if level == 'E' or level == 'EASY':
        print('Easy difficulty selected!\n')
        questions = 2
        quantity = 3
        minimum, maximum = 1, 5
        break
    elif level == 'M' or level == 'MEDIUM':
        print('Medium difficulty selected!\n')
        questions = 4
        quantity = 5
        minimum, maximum = 3, 12
        break
    elif level == 'H' or level == 'HARD':
        print('Hard difficulty selected!\n')
        questions = 6
        quantity = 8
        minimum, maximum = 10, 25
        break
    else:
        print('Invalid choice! Enter E, M or H.')

# Initialise variable score to keep track of the user's correct answers
score = 0

# Loop over a specific number of times. Number of iterations are
# controlled by the difficulty the user chooses
for i in range(questions):
    print(f'Question {i + 1} of {questions}.')

    # User is up to last question and are presented with the Challenge Question
    if i + 1 == len(range(questions)):
        print('Challenge Question!')
        # The Challenge Question uses double the minimum and double the maximum
        number_list = random_list(quantity, minimum * 2, maximum * 2)
    # User is not up to last question
    else:
        number_list = random_list(quantity, minimum, maximum)

    # Randomly show the user different types of questions
    question_type = random.randint(1, 4)
    if question_type == 1:
        print(f'What is the smallest number in this list? {number_list}')
        answer = min(number_list)
    elif question_type == 2:
        print(f'What is the biggest number in this list? {number_list}')
        answer = max(number_list)
    elif question_type == 3:
        print(f'What is the sum of the numbers in this list? {number_list}')
        answer = sum(number_list)
    elif question_type == 4:
        print(f'What is the average of the numbers in this list? {number_list}')
        average = statistics.mean(number_list)  # First calculate the average of the numbers in random list
        answer = math.ceil(average)             # Round up the answer to nearest integer

    # Get user input and validate it.
    # If user does not enter an integer continue re-prompting for correct input
    while True:
        try:
            user_response = int(input('> '))
            if user_response == answer:
                print('Correct!\n')
                score += 1
            else:
                print(f'Incorrect! Correct answer was {answer}\n')
            break
        except ValueError:
            print('Try again! Use only an integer.\n')

# Test is complete and the user can see their score
print('Test Complete!')
print(f'You scored {score}/{questions} ({score/questions * 100}%)')
