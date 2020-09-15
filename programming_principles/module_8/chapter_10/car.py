class Car:

    def __init__(self, init_year_model, init_make):
        self.set_year_model(init_year_model)
        self.set_car_make(init_make)
        self.__speed = 0  # Current speed of the car is 0

    def set_year_model(self, year_model):
        self.__year_model = int(year_model) 

    def set_car_make(self, car_make):
        self.__make = car_make 

    def accelerate(self):
        self.__speed += 5  # Increase car's speed by 5

    def brake(self):
        self.__speed -= 5  # Decrease car's speed by 5

    def get_speed(self):
        return self.__speed
