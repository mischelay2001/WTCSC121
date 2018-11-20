__author__ = 'Michele Johnson'

""" Create a MegaMeal class.  This class is a derived class of the ExpressMeal class. 
It has two additional protected instance variables: drink and dessert.  Define a chooseDrink method to choose drink, 
a chooseDessert method to choose dessert, and a displayOrder method to display items ordered.

MealMega
    -meat_choice: Integer
    -side_choice: Integer
    +create(meat_choice: Integer, meat_side: Integer)
    +setChoiceText(): String, String
    +entry_choice_meat(): Integer
    +entry_choice_side(): Integer """

from meal_express import MealExpress

from CSC121FinalProject_WakeMartUpgrade import valid_entry


class MealMega(MealExpress):


    def __init__(self):
        base = super()
        base.__init__()

        """ constructor of class MealMega """

        self.__drink_choice = entry_choice_drink()
        self.__dessert_choice = entry_choice_dessert()
        self.__drink_text = ""
        self.__dessert_text = ""


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

    def setChoiceTextMega(self):

        if self.__drink_choice == 1:
            self.__drink_text = "Soda"
        if self.__drink_choice == 2:
            self.__drink_text = "Iced Tea"
        if self.__dessert_choice == 1:
            self.__dessert_text = "Ice Cream"
        if self.__dessert_choice == 2:
            self.__dessert_text = "Cookie"

        return self.__drink_text, self.__dessert_text


    def __str__(self):
        """ convert class to string """

        return '\nMeat Choice\t\t' + str(self._meat_choice) + ":  " + self._meat_text \
               + '\nSide Choice\t\t' + str(self._side_choice) + ":  " + self._side_text \
               + '\nDrink Choice\t' + str(self.__drink_choice) + ":  " + self.__drink_text \
               + '\nDessert Choice\t' + str(self.__dessert_choice) + ":  " + self.__dessert_text


def entry_choice_drink():
    """ gets valid menu choice """

    a_choice = 0
    is_valid = False
    while is_valid is False:
        print("\nMenu:\n"
              "\t 1 for Soda\n"
              "\t 2 for Iced Tea\n")
        request_text = "Enter drink selection"
        a_choice = valid_entry.integer_entry(request_text)

        if a_choice < 1 or a_choice > 2:
            print("\nNot a valid selection.\n"
                  "Please try again.\n")
        else:
            is_valid = True

    return a_choice


def entry_choice_dessert():
    """ gets valid menu choice """

    a_choice = 0
    is_valid = False
    while is_valid is False:
        print("\nMenu:\n"
              "\t 1 for Ice Cream\n"
              "\t 2 for Cookie\n")
        request_text = "Enter dessert selection"
        a_choice = valid_entry.integer_entry(request_text)

        if a_choice < 1 or a_choice > 2:
            print("\nNot a valid selection.\n"
                  "Please try again.\n")
        else:
            is_valid = True

    return a_choice

