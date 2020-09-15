"""
Create an object of the class and prompts the user to enter
name
type
age of the pet
Store the data as object's attributes
Retrieve the data using the accessor methods to get the attributes
and display the data on the screen
"""
import pet

def main():
    pet_name = input("Enter your pet's name: ")
    pet_type = input("Enter your pet's type: ")
    pet_age = int(input("Enter your pet's age: "))

    user_pet = pet.Pet(pet_name, pet_type, pet_age)

    print('Here is the data about your pet')
    print(user_pet)


if __name__ == '__main__':
    main()
