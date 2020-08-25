import random

while True:
    test_type = input('Enter test type: ')
    if test_type == '+':
        print('Addition Test\n')
        break
    elif test_type == '-':
        print('Subtraction Test\n')
        break
    else:
        print('Invalid input.')

num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)