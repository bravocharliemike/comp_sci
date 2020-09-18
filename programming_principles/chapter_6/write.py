def main():
    filename = 'scores.txt'
    fout = open(filename, 'w')
    keep_going = 'y'

    while keep_going == 'y':
        
        print('Enter the data for each score')
        name = input('Name: ')
        score = input('Score: ')

        # Write the data to the file
        fout.write(name + '\n')
        fout.write(score + '\n')

        # Keep going?
        keep_going = input('Do you wish to keep goin? y/n: ')

    fout.close()

main()
