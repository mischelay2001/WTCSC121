__author__ = 'Michele Johnson'

""" Program requirements:
#
# A fast food restaurant has two types of meals for customers to choose.  An express meal includes meat and side item.  
A mega meal includes meat, side item, drink and dessert.  
There are two meat choices (chicken sandwich or cheese burger), two side item choices (fries or chips), 
two drink choices (soda or iced tea) and two dessert choices (ice-cream or cookie).  
They need a program to place order.  You Python project needs to follow these requirements:

(a)	Create an ExpressMeal class.  This class has two protected instance variables: meat and side.  
Define a chooseMeat method to choose meat, a chooseSide method to choose side item, 
and a displayOrder method to display items ordered.

(b)	Create a MegaMeal class.  This class is a derived class of the ExpressMeal class. 
It has two additional protected instance variables: drink and dessert.  Define a chooseDrink method to choose drink, 
a chooseDessert method to choose dessert, and a displayOrder method to display items ordered.

(c)	In the main module, ask user to choose either express meal or mega meal.  
Create an object and call its methods to input and display items chosen by the customer.
  """

from meal_express import MealExpress
from meal_mega import MealMega

from CSC121FinalProject_WakeMartUpgrade import valid_entry


def main():
    # Introduce Program
    print("MEAL ORDER\n")
    print("Program will take an order per the user's choices.\n")

    # Initialize variable
    meal_choice = valid_entry.entry_meal_choice()

    if meal_choice == 1:
        # Get user choices and initialize MealExpress class
        a_meal_express = MealExpress()

        # Converts user integer input into corresponding choices as strings
        meat, side = a_meal_express.setChoiceText()

        # Displays ordered choices Express
        print(a_meal_express)


    if meal_choice == 2:
        # Get user choices and initialize MealMega class
        a_meal_mega = MealMega()

        # Converts user integer input into corresponding choices as strings
        meat, side = a_meal_mega.setChoiceText()
        drink, dessert = a_meal_mega.setChoiceTextMega()


    if meal_choice == 2:

        # Displays ordered choices Mega
        print(a_meal_mega)

main()
