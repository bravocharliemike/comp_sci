class Employee:

    def __init__(self, init_name, init_id_num, init_dept, init_job_title):
        self.set_name(init_name)
        self.set_id_number(init_id_num)
        self.set_department(init_dept)
        self.set_job_title(init_job_title)

    def __str__(self):
        result = 'Name: ' + self.get_name() + \
                '\nID number: ' + self.get_id_number() + \
                '\nDepartment: ' + self.get_department() + \
                '\nTitle: ' + self.get_job_title()
        return result

    def set_name(self, new_name):
        self.__name = new_name.title()

    def set_id_number(self, new_id_num):
        self.__id_number = new_id_num

    def set_department(self, new_dept):
        self.__department = new_dept

    def set_job_title(self, new_title):
        self.__job_title = new_title

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title
