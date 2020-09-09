import pprint

students = {
        60254: 'John Smith',
        60255: 'Gert Du-Cart',
        60256: 'Sun Po',
        60257: 'Bort Woods',
        60258: 'Andrew Butters',
        60259: 'Betty Ho'
        }

# ------ Begin program -------
usernames = dict()

for k, v in students.items():
    v = v.lower().replace('-', '')
    first_name, surname = v.split()[0], v.split()[1]
    username = first_name[0] + surname[0:4]
    username = username.ljust(5, '0')
    usernames[k] = username

print('This is the students dict')
pprint.pprint(students)
print()
print('And this is the usernames dict')
pprint.pprint(usernames)
# ------ Pseudocode -------
# Create an empty dictionary called usernames
# Loop over the students dictionary to access the names:
    #Convert the first name and surname to lowercase
    #Delete any specials characters like dashes
    #Split the two words in the values and store the first one as first_name and the second as surname
    #Take the first letter of the first_name and four letter of the surname and store that as username
    #If the length of the username is less than 5:
        #Add zeroes to the end

    #Create a new key in usernames dict and the value is username


