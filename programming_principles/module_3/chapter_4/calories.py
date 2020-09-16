# 4.2 calories per minute
# display calories burnt after 10, 15, 20, 25 and 30 minutes

CALORIES_BURNT = 4.2

print('Minutes\t\tCalories Burnt')

for i in range(10, 31, 5):
    burnt = CALORIES_BURNT * i
    print(f'{i}\t\t{burnt}') 
