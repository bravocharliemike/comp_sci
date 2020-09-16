keep_going = 'y'

while keep_going == 'y':
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print(num1 + num2)
    
    # Continue?
    keep_going = input('Do you want to continue? (Enter y for yes): ').lower()
