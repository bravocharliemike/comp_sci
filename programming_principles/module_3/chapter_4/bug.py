total_bugs = 0

for i in range(5):
    bugs_collected = int(input(f'How many bugs did you collect on day {i+1}? '))
    total_bugs += bugs_collected

# Display total number of bugs
print(f'Total number of bugs collected: {total_bugs}')
