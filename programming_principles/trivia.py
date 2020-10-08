import json

# ------ Function definitions -------
def load_file_data(name):
    try:
        with open(name, 'r') as fin:
            data = json.load(fin)
    except FileNotFoundError:
        data = []
    return data

def input_int(prompt):
    while True:
        num = input(prompt)
        try:
            num = int(num)
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
    try:
        with open(filename, 'w') as fout:
            json.dump(data_list, fout, indent=4)
    except FileNotFoundError:
        print(f'The file {filename} does not exist.')

def list_questions(data_list):
    if len(data_list) == 0:  # There are no questions in the list
        print('There are no questions saved.')
    else:
        print('Current questions:')
        for index, question in enumerate(data_list):
            print(f"\t{index + 1}) {question['question']}")

# ------ Beginning of program ------
# Load the data file with the questions
FILENAME = 'data.txt'
data = load_file_data(FILENAME)

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

        question_dict = {
                'question': question,
                'answers': answers,
                'difficulty': difficulty
                }
        data.append(question_dict)  # Add the new question to the list

        save_data(data)  # Save the questions to the file

    # --- USER CHOOSES TO LIST QUESTIONS
    if user_selection == 'l':
        list_questions(data)



