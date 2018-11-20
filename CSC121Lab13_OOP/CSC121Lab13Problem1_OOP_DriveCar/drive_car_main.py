__author__ = 'Michele Johnson'

""" Program requirements:
#
# Create a Python project DriveCar.  Add a Python file employee.py to this project.  Define a class Car in this file.  
# In this class, create three publicly accessible instance variables to store the car’s make, model, and speed.  
# Also define the following methods:
# 
# (a)	A __init__ method that accepts car’s make and model as arguments.  
# Write statements in __init__ to store them in instance variables.  
# Also create an instance variable for speed and initialize it to 0.

# (b)	An accelerate method to increase the speed of the car by 5 mph.  
# This method has no parameters and no return value.

# (c)	A decelerate method to decrease the speed of the car by 5 mph.  
# This method needs to ensure that the speed will never go below 0. It has no parameters and no return value. 

Add a file driveCar_main.py to this project.  This is the main module.  
Write code to ask the user to enter model and make of a car.  Create an instance of Car.  
Display the initial speed of the car.  Write a loop to control the speed of the car.  
In the loop, ask the user to enter 1 for acceleration, 2 for deceleration or 3 for exit.  
Every time the speed of the car changes, display the speed.  """

from car import Car


def main():
    # Introduce Program
    print("DRIVE CAR\n")
    print("Program will track the speed of a car per the selection to accelerate or decelerate.\n")

    # Initialize variables
    user_choice = 0

    # Get user entries
    entry_make = str(input("Enter car make:\t\t"))
    entry_model = str(input("Enter car model:\t"))

    # Initialize Car class
    a_car = Car(entry_make, entry_model)
    print("Current speed:\t   ", a_car.speed, "\n")

    # Loop until user selects to exit
    while user_choice != 3:

        # Get valid menu choice
        user_choice = a_car.entry_choice()

        # Handle menu selection
        if user_choice == 3:
            print("\nFinal speed:\t\t", a_car.speed)
        else:
            if user_choice == 1:
                a_car.accelerate()
            elif user_choice == 2:
                a_car.decelerate()
            print("Current speed:\t\t", a_car.speed, "\n")


main()
