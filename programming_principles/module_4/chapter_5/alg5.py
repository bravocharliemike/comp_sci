def my_function(x, y):
    return x[y]

# Passing arguments as keywords
test = my_function(x='testing', y=2)

# What will be printed after retrieving "test"?
# the answer is the string of character 's' because testing[2] = 's'
print(test)
