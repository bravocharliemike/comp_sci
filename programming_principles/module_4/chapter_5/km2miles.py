CONVERSION_RATE = 0.6214  # km to miles

def main():

    kilometres = float(input('Enter the distance in kilometres: '))
    km_to_miles(kilometres)

def km_to_miles(distance):
    result = distance * CONVERSION_RATE
    print('The conversion of', format(distance, '.2f'), 'kilometres')
    print('to miles is', format(result, '.2f'), 'miles.')


if __name__ == '__main__':
    main()
