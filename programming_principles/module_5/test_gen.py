import random

while True:
    test_type = input('Enter "+" or "-": ')
    if test_type == '+':
        print('Addition Test\n')
        break
    elif test_type == '-':
        print('Subtraction Test\n')
        break
    else:
        print('Invalid input!')

print('Name: _________________\n\n')

# This list will keep track of questions asked by the generator
questions = []
for i in range(10):
    while True:
        num_1 = random.randint(0, 9)
        num_2 = random.randint(0, 9)

        if (test_type == '-') and (num_2 > num_1):
            num_1, num_2 = num_2, num_1

        # Tuple holds the generated random numbers
        current_question = (num_1, num_2)
        # Check if the question has been asked already
        if current_question not in questions:
            break

    print(f'{num_1} {test_type} {num_2} = ___________\n')
    questions.append(current_question)