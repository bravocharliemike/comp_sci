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

for i in range(10):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)

    print(f'{num_1} {test_type} {num_2} = ___________\n')