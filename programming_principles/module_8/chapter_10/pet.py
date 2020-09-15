class Pet:
    
    def __init__(self, init_name, init_type, init_age):
        self.set_name(init_name)
        self.set_animal_type(init_type)
        self.set_age(init_age)

    def __str__(self):
        return f'Name: {self.__name}\nType: {self.__animal_type}\nAge: {self.__age}'

    # Mutator methods
    def set_name(self, new_name):
        self.__name = new_name

    def set_animal_type(self, new_type):
        self.__animal_type = new_type

    def set_age(self, new_age):
        self.__age = new_age

    # Accessors methods
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
