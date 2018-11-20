__author__ = 'Michele Johnson'

""" Write a new version of the DriveCar project you wrote in Problem 1.  
Create a new Python project DriveCarNew and copy the files from the old project.  
Make the following changes to class Car:

(a)	Change all instance variables to private
(b)	Write getter method for speed.
(c)	Define a __str__ method to display the car’s make, model and speed.

Car
    -make: String
    -model: String
    -speed: Integer
    +create(car_make: String)
    +accelerate(): Integer
    +decelerate(): Integer
    +getSpeed(): Integer
    +entry_choice(): Integer  """

from Lab14_OOP2_Problem1_MealOrderTemp.valid_entry import integer_entry


class Car:

    """ Creates three private instance variables to store the car’s make, model, and speed """

    def __init__(self, car_make, car_model):

        """ constructor of class Car """

        self.__make = car_make
        self.__model = car_model
        self.__speed = 0

    def accelerate(self):

        """ increases speed by 5 """

        self.__speed += 5

    def decelerate(self):

        """ decreases speed by 5"""

        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):

        """ gets and returns speed"""
        return self.__speed

    def __str__(self):

        """ converts class to string """
        return '\nMake:\t\t\t' + self.__make + '\nModel:\t\t\t' + self.__model + '\nFinal speed:\t' + str(
            self.__speed)

    def entry_choice(self):

        """ gets valid menu choice """

        a_choice = 0
        is_valid = False
        while is_valid is False:
            print("Menu:\n"
                  "\t 1 to Accelerate\n"
                  "\t 2 to Decelerate\n"
                  "\t 3 to Exit")
            request_text = "Enter selection"
            a_choice = integer_entry(request_text)

            if a_choice < 1 or a_choice > 3:
                print("\nNot a valid selection.\n"
                      "Please try again.\n")
            else:
                is_valid = True

        return a_choice
