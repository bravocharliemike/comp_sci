import random

"""
This is a test comment !!!
"""


def random_list(quantity, minimum, maximum):
    """
    Sets a random list ....
    :param quantity:
    :param minimum:
    :param maximum:
    :return: list with quantity random integers between minimum and maximum
    """
    final_list = [random.randint(minimum, maximum) for number in range(quantity)]
    return final_list

# Initialise a pool of questions to ask the user
question_list = [
    'Q1',
    'Q2',
    'Q3',
    'Q4',
    'Q5'
]

print('Welcome to the Number List Test program')
while True:
    level = input('Select a difficulty:\n'
                  '[E]asy\n'
                  '[M]edium\n'
                  '[H]ard\n'
                  '> ')
    if level.upper() == 'E':
        set_difficulty_level('E')
        break
    elif level.upper() == 'M':
        set_difficulty_level('M')
        break
    elif level.upper() == 'H':
        set_difficulty_level('H')
        break
    else:
        print('Invalid choice! Enter E, M or H.')


score = 0
for index, question in enumerate(range(questions)):
    print(f'Question {index + 1} of {questions}')
    question = random.choice(question_list)
    numbers_list = random_list(quantity, minimum, maximum)
    print(f'!!! These are the numbers to challenge the user --> {numbers_list}')
    # TODO Get user response and compare to right answer
    # TODO Generate challenge question

# TODO Finalise the test and show the score