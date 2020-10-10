
def load_file_data(name):
    import json
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

def search_question(data_list, search_query):
    found = False
    for index, question in enumerate(data_list):
        question_text = question['question']
        if search_query in question_text.lower():
            found = True
            print(f'\t{index + 1}) {question_text}')
    if not found:
        print('No results found.')

def view_question(data_list, num):
    if len(data_list) < 1:
        print('There are no questions saved.')
    else:
        try:
            result = data_list[num - 1]  # Subtract one to correspond to index
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
