import pprint
import json

def resolve_duplicates(usernames, username):
    counter = 0
    while True:
        counter += 1
        new_username = username + str(counter)
        if new_username not in usernames:
            return new_username


students = {
        60254: 'John Smith',
        60255: 'Gert Hans-Dyer',
        60256: 'Sun Po',
        60257: 'Bort Woods',
        60258: 'Andrew Butters',
        60259: 'Betty Ho',
        60260: 'Jonah Smithers',
        60261: 'Sha Po',
        60262: 'Jane Smitt'
        }

# ------ Begin program -------
usernames = dict()

for k, v in students.items():
    full_name = v.lower().replace('-', '')
    first_name, surname = full_name.split()[0], full_name.split()[1]
    username = first_name[0] + surname[0:4]
    username = username.ljust(5, '0')

    if username in usernames.values():
        username = resolve_duplicates(usernames.values(), username)

    usernames[k] = username

# Printing the final usernames dict
pprint.pprint(usernames)

# Writing to a text file in JSON format
with open('usernames.txt', 'w') as fout:
    json.dump(usernames, fout, indent=4)
    




