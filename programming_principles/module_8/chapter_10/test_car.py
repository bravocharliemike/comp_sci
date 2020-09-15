import car

def main():
    corolla = car.Car(2015, 'Toyota')

    # Time to speed up
    for i in range(5):
        corolla.accelerate()
        print('The current speed is')
        print(corolla.get_speed())

    # Time to slow down
    for i in range(5):
        corolla.brake()
        print('The current speed is')
        print(corolla.get_speed())


if __name__ == '__main__':
    main()
