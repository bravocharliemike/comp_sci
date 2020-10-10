""" 
# Data list, Number -> String
# Takes a list of dicts and a number and outputs the question requested by user

# Stub
def view_question(data_list, num):
    print several strings


"""

data = [
    {
        "question": "In which year was Halley's Comet last visible from Earth?",
        "answers": [
            "1986"
        ],
        "difficulty": 3
    },
    {
        "question": "Where were the 2016 Summer Olympics held?",
        "answers": [
            "rio de janeiro",
            "rio",
            "brazil"
        ],
        "difficulty": 2
    },
    {
        "question": "How many fingers in the human hand?",
        "answers": [
            "10",
            "ten"
        ],
        "difficulty": 2
    }
]

def view_question(data_list, num):
    if len(data_list) < 1:
        print('There are no questions saved.')
    else:
        result = data_list[num - 1]  # Subtract one to correspond to index
        answers_string = ', '.join(result['answers']).title()

        print('\nQuestion:')
        print(f'\t{result["question"]}\n')

        if len(result['answers']) > 1:
            print(f'Answers: {answers_string}')
        else:
            print(f'Answer: {answers_string}')

        print(f'Difficulty: {result["difficulty"]}\n')


def main():
    x = int(input('Enter a question number: '))

    view_question(data, x)

if __name__ == '__main__':
    main()
