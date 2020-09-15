import employee

def main():
    
    print('Name\t\tID Number\t\tDepartment\t\tJob Title')

    employees = [ 
            employee.Employee('Susan Meyers', 47899, 'Accounting', 'Vice President'),
            employee.Employee('Mark Jone', 39119, 'IT', 'Programmer'),
            employee.Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')
            ]

    for worker in employees:
        print(worker)


if __name__ == '__main__':
    main()
