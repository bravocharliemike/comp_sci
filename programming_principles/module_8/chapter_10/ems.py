import employee
import json

FILENAME = 'management_system.json'
# Constants to use as user choices
LOOK_UP = 1
ADD = 2
EDIT = 3
DELETE = 4
QUIT = 5


def main():
    
    employees = load_data()

    choice = None

    while choice != QUIT:
        choice = get_user_choice()

        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add_employee(employees)
        elif choice == EDIT:
            print('editing')
        elif choice == DELETE:
            print('deleting')
        
    save_data(employees)

# ---- Function definitions
def load_data():
    try:
        fin = open(FILENAME, 'r')
        employees_dict = json.load(fin)
        fin.close()
    except FileNotFoundError:
        employees_dict = dict()
        new_file = open(FILENAME, 'w')
        json.dump(employees_dict, new_file)
        new_file.close()
            
    return employees_dict
        
def look_up(employees):
    # Get the employee ID to lookup
    id_num = input('Enter the employee ID: ')
    print(employees.get(id_num, 'ID does not exist'))

def add_employee(employees):
    # Get relevant information about new employee
    name = input('Enter employee name: ')
    id_number = input('Enter employee ID number: ')
    department = input('Enter employee department: ')
    job_title = input('Enter employee job title: ')

    new_emp = employee.Employee(name, id_number, department, job_title)
    
    if id_number not in employees:
        employees[id_number] = new_emp
    else:
        print('That employee already exists.')



def get_user_choice():
    # Display menu for user selection
    print()
    print('Menu'.center(30))
    print('-' * 30)
    print('1. Look up an employee.')
    print('2. Add an employee.')
    print('3. Edit an existing employee.')
    print('4. Delete an employee.')
    print('5. Quit the program.\n')

    choice = int(input('Enter your choice: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Invalid choice.\n' \
                'Please try again: '))
    return choice

def save_data(data):
    with open(FILENAME, 'w') as fout:
        json.dump(data, fout, indent=4)


# ---- Begin main loop
if __name__ == '__main__':
    main()
