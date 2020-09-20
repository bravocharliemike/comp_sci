
words = [   'hello',
            'world',
            'superfluous',
            'hi',
            'text',
            'major',
            'abstain',
            'itinerary',
            'nine',
            'filename',
        ]

total_length = 0
for idx, word in enumerate(words, 1):
    print(idx, word, len(word))
    total_length += len(word)
    print(f'Total length is now {str(total_length)}')
    
print(f'Total length is at the end {str(total_length)}')
print(total_length / len(words))

