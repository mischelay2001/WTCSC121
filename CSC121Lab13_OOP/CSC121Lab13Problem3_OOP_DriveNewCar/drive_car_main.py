__author__ = 'Michele Johnson'

""" Program requirements:

Write a new version of the DriveCar project you wrote in Problem 1.  
Create a new Python project DriveCarNew and copy the files from the old project.  
Make the following changes to class Car:

(a)	Change all instance variables to private
(b)	Write getter method for speed.
(c)	Define a __str__ method to display the car’s make, model and speed.

Do the following in the main module:

(a)	Get make and model from the user and use the input data to create an instance of Car
(b)	Display the Car instance with a print statement
(c)	Write a loop to allow the user to control the speed of the car just like the old project. """

from car import Car


def main():

    # Introduce Program
    print("DRIVE CAR II\n")
    print("Program will track the speed of a car per the selection to accelerate or decelerate.\n")

    # Initialize variables
    user_choice = 0

    # Get user entries
    entry_make = str(input("Enter car make:\t\t"))
    entry_model = str(input("Enter car model:\t"))

    # Initialize Car class
    a_car = Car(entry_make, entry_model)
    a_car.speed = a_car.get_speed()
    print("Current speed:\t    ", a_car.speed, "\n")

    # Loop until user selects to exit
    while user_choice != 3:

        # Get valid menu choice
        user_choice = a_car.entry_choice()

        # Handle menu selection
        if user_choice == 3:
            print(a_car)
        else:
            if user_choice == 1:
                a_car.accelerate()
            elif user_choice == 2:
                a_car.decelerate()
            print("Current speed:\t\t", a_car.get_speed(), "\n")


main()
