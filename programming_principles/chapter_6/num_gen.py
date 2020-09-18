filename = 'numbers.txt'

with open(filename, 'w') as fout:
    for i in range(1, 101):
        fout.write(str(i) + '\n')
