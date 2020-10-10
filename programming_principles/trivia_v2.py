import json
import manager

# ------ Beginning of program ------
# Load the data file with the questions
FILENAME = 'data.txt'
data = manager.load_file_data(FILENAME)

# ------ Main loop -------

print('Welcome to the Quiz Admin Program')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit')
    user_selection = input('> ').lower()

    if user_selection == 'a':
        question = manager.input_something('Enter a question: ')

        answers = []
        answer = None  # Used to check the condition to get out of loop

        while True:
            answer = manager.input_something('Enter a valid answer (enter "q" to quit): ').lower()
            if answer == 'q':
                break
            answers.append(answer)

        while True:
            difficulty = manager.input_int('Enter question difficulty (1-5): ')
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

        manager.save_data(data)  # Save the questions to the file

    # --- USER CHOOSES TO LIST QUESTIONS
    elif user_selection == 'l':
        manager.list_questions(data)

    # --- USER CHOOSES TO SEARCH FOR QUESTIONS
    elif user_selection == 's':
        search_term = manager.input_something('Enter a search term: ').lower()
        manager.search_question(data, search_term)

    # --- USER WANTS TO VIEW A QUESTION
    elif user_selection == 'v':
        question_number = manager.input_int('Question number to view: ')
        manager.view_question(data, question_number)

    # --- USER WANTS TO EXIT
    elif user_selection == 'q':
        print('Goodbye!')
        break

    # --- User enters invalid choice
    else:
        print('Invalid choice')
        continue
