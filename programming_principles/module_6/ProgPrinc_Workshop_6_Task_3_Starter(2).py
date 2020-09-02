# --- getList(filename), returns a list of strings ---
# (open/create file and return lines of text as a list of strings)
def get_list(filename):
    try:
        fin = open(filename, 'r')   # Try to open the file in read mode
    except FileNotFoundError:
        fin = open(filename, 'w+')  # Create the file it it doesn't exist

    data = fin.readlines()
    fin.close()
    return data


# --- showList(data), returns nothing ---
# (receive list of strings and display them, or "nothing in list" message)
def show_list(data):
    if len(data) == 0:
        print('Your To Do List is empty.')

    else:
        print('To Do List:')
        for index, task in enumerate(data):
            print(f'\t{index + 1}) {task.rstrip()}')


# --- add_to_list(filename, data), returns a list of strings ---
# (prompt for an item to add to the list of strings and append to the file)
def add_to_list(filename, data):
    task = input('Add: ')
    data.append(task)

    fout = open(filename, 'a')
    fout.write(task + '\n')
    fout.close()
    print('Item added to list.')
    return data


# --- deleteFromList(filename, data), returns a list of strings ---
# (prompt for item number to delete from the list of strings and write list to the file)
def delete_from_list(filename, data):
    target = input('Item number to delete: ')
    try:
        target = int(target)
        del data[target - 1]    # Subtract 1 from target so it matches list index
    except:
        print('Invalid input - Nothing deleted.\n')
        return data

    fout = open(filename, 'w')
    fout.writelines(data)
    fout.close()

    print('Item deleted from list.')
    return data


# --- main part of program ---
FILENAME = 'list.txt'           # define the filename used to store the list
line_list = get_list(FILENAME)   # call the getList function to read the file into a list'

while True:     # this endless loop displays the list and prompts the user for a command

    show_list(line_list)    # call showList to show the current content of the list

    # show the instructions for the possible commands - [a]dd, [d]elete, e[x]it
    print('\nType "a" to add an item.')

    if len(line_list) > 0:  # only show the delete instruction if the list has items
        print('Type "d" to delete an item.')

    print('Type "x" to exit.')

    command = input('> ')   # prompt for a command

    # if "a", call addToList to prompt for item and add to list
    if command == 'a': 
        line_list = add_to_list(FILENAME, line_list)

    # if "d", call deleteFromList to prompt for item number and delete from list        
    elif command == 'd' and len(line_list) > 0:
        line_list = delete_from_list(FILENAME, line_list)

    elif command == 'x':    # if "x", break out of the loop to end the program
        print('Goodbye!')
        break

    else: # if anything else, show an error message
        print('Invalid command.\n')
