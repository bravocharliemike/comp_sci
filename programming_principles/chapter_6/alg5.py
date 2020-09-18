"""
Chapter 5: Algorithm workbench 5
Modify the code from problem 4 so it adds all of the numbers read from the
file and displays their total
"""

filename = 'number_list.txt'

with open(filename) as fin:
    data = fin.read()
    nums = data.split()
    
total = 0
for num in nums:
    total += int(num)

print(total)
        
