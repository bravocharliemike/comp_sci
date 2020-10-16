import json

# ------ Function definitions -------
def input_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 1:
                continue
        except ValueError:
            continue
        return num

def input_something(prompt):
    while True:
        answer = input(prompt)
        if not answer.strip():
            continue
        return answer

def save_data(data_list):
    filename = 'data.txt'
    with open(filename, 'w') as fout:
        json.dump(data_list, fout, indent=4)

####################################
# ------ BEGINNING OF PROGRAM ------
####################################

# Load the data file with the questions
FILENAME = 'data.txt'
try:
    with open(FILENAME, 'r') as fin:
        data = json.load(fin)
except FileNotFoundError:
    data = []

# ------ Main loop -------

print('Welcome to the Quiz Admin Program')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit')
    user_selection = input('> ').lower()

    if user_selection == 'a':
        question = input_something('Enter a question: ')

        answers = []
        answer = None  # Used to check the condition to get out of loop

        while True:
            answer = input_something('Enter a valid answer (enter "q" to quit): ').lower()
            if answer == 'q':
                break
            answers.append(answer)

        while True:
            difficulty = input_int('Enter question difficulty (1-5): ')
            if (difficulty >= 1) and (difficulty <= 5):
                break
            print('Invalid value. Must be an integer between 1 and 5')

        question_dict = {
                'question': question,
                'answers': answers,
                'difficulty': difficulty
                }
        data.append(question_dict)  # Add the new question to the list
        print('Question added!')

        save_data(data)  # Save the questions to the file

    # --- USER CHOOSES TO LIST QUESTIONS
    elif user_selection == 'l':
        if not data:
            print('There are no questions saved.')
            continue
        print('Current questions:')
        for index, question in enumerate(data):
            print(f"\t{index + 1}) {question['question']}")

    # --- USER CHOOSES TO SEARCH FOR QUESTIONS
    elif user_selection == 's':
        if not data:
            print('There are no questions saved.')
            continue
        search_term = input_something('Enter a search term: ').lower()
        found = False

        for index, question in enumerate(data):
            question_text = question['question']
            if search_term in question_text.lower():
                found = True
                print(f'\t{index + 1}) {question_text}')
        if not found:
            print('No results found.')

    # --- USER WANTS TO VIEW A QUESTION
    elif user_selection == 'v':
        if not data:
            print('There are no questions saved.')
            continue

        question_number = input_int('Question number to view: ')
        try:
            result = data[question_number - 1]  # Subtract one to correspond to index  # Go back to the top of the main loop
            answers_string = ', '.join(result['answers']).title()

            print('\nQuestion:')
            print(f'\t{result["question"]}\n')
            if len(result['answers']) > 1:
                print(f'Answers: {answers_string}')
            else:
                print(f'Answer: {answers_string}')
            print(f'Difficulty: {result["difficulty"]}')
        except IndexError:
            print('Invalid index number')

    # --- USER WANTS TO DELETE A QUESTION
    elif user_selection == 'd':
        if not data:
            print('There are no questions saved.')
            continue

        question_to_delete = input_int('Question number to delete: ')
        try:
            del data[question_to_delete - 1]
            print('Question deleted!')
        except IndexError:
            print('Invalid index number')

        save_data(data)  # Save the updated file without the deleted question

    # --- USER WANTS TO EXIT
    elif user_selection == 'q':
        print('Goodbye!')
        break

    # --- USER ENTERS INVALID CHOICE
    else:
        print('Invalid choice')
        continue
