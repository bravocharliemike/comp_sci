def count_words(filename):
    try:
        with open(filename) as fin:
            contents = fin.read()
    except FileNotFoundError:
        print(f'The file {filename} does not exist.')
    else:
        words = contents.split()
        print(f'The file {filename} has about {len(words)} words in total.')


filenames = ['alice.txt', 'moby_dick.txt', 'random.txt']

for fin in filenames:
    count_words(fin)


