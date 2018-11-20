__author__ = 'Michele Johnson'

""" Create an ExpressMeal class.  This class has two protected instance variables: meat and side.  
Define a chooseMeat method to choose meat, a chooseSide method to choose side item, 
and a displayOrder method to display items ordered.

MealExpress
    -meat_choice: Integer
    -side_choice: Integer
    +create(meat_choice: Integer, meat_side: Integer)
    +setChoiceText(): String, String
    +entry_choice_meat(): Integer
    +entry_choice_side(): Integer """

from CSC121FinalProject_WakeMartUpgrade import valid_entry


class MealExpress:
    """ Creates two protected instance variables to store the user's meat and side choices """

    def __init__(self):
        """ constructor of class MealExpress"""

        self._meat_choice = entry_choice_meat()
        self._side_choice = entry_choice_side()
        self._meat_text = ""
        self._side_text = ""

    def setChoiceText(self):

        if self._meat_choice == 1:
            self._meat_text = "Chicken"
        if self._meat_choice == 2:
            self._meat_text = "Cheeseburger"
        if self._side_choice == 1:
            self._side_text = "Fries"
        if self._side_choice == 2:
            self._side_text = "Chips"

        return self._meat_text, self._side_text

    def __str__(self):
        """ convert class to string """

        return '\nMeat Choice\t\t' + str(self._meat_choice) + ":  " + self._meat_text + '\nSide Choice\t\t' \
               + str(self._side_choice) + ":  " + self._side_text


def entry_choice_meat():
    """ gets valid menu choice """

    a_choice = 0
    is_valid = False
    while is_valid is False:
        print("\nMenu:\n"
              "\t 1 for Chicken\n"
              "\t 2 for Cheeseburger\n")
        request_text = "Enter meat selection"
        a_choice = valid_entry.integer_entry(request_text)

        if a_choice < 1 or a_choice > 2:
            print("\nNot a valid selection.\n"
                  "Please try again.\n")
        else:
            is_valid = True

    return a_choice


def entry_choice_side():
    """ gets valid menu choice """

    a_choice = 0
    is_valid = False
    while is_valid is False:
        print("\nMenu:\n"
              "\t 1 for Fries\n"
              "\t 2 for Chips\n")
        request_text = "Enter side selection"
        a_choice = valid_entry.integer_entry(request_text)

        if a_choice < 1 or a_choice > 2:
            print("\nNot a valid selection.\n"
                  "Please try again.\n")
        else:
            is_valid = True

    return a_choice
