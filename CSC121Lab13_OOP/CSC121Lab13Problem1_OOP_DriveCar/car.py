__author__ = 'Michele Johnson'

""" Add a Python file employee.py to this project.  Define a class Car in this file.  
In this class, create three publicly accessible instance variables to store the car’s make, model, and speed.

Car
    +make: String
    +model: String
    +speed: Integer
    +create(car_make: String)
    +accelerate(): Integer
    +decelerate(): Integer
    +entry_choice(): Integer  """

from Lab14_OOP2_Problem1_MealOrderTemp.valid_entry import integer_entry


class Car:

    """ Creates three publicly accessible instance variables to store the car’s make, model, and speed """

    def __init__(self, car_make, car_model):

        """ constructor of class Car """

        self.make = car_make
        self.model = car_model
        self.speed = 0

    def accelerate(self):

        """ increases speed by 5 """

        self.speed += 5

    def decelerate(self):

        """ decreases speed by 5"""

        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

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
