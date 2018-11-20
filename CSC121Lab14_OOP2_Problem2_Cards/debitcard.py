__author__ = 'Michele Johnson'

""" (c)	Create a DebitCard class.  This class is a derived class of the Card class. 
It has two additional private instance variables: pin and fund_available.  
Define an inputInfo method to input PIN code and fund available to use, and a  
displayInfo method to display these two items."""

from card import CardUser


class DebitCard(CardUser):
    """ Creates instance variables """

    def __init__(self):
        base = super()
        base.__init__(self, card_number, card_user)

        """ constructor"""

        self.__card_pin = 0.0
        self.__funds_available = 0.0


    def inputInfo(self):
        self.__card_pin = float(input("Enter PIN number\t"))
        self.__funds_available = float(input("Enter funds available\t"))
    
    
    def displayInfo(self):
        print("Card PIN:\t", self.__card_pin)
        print("Available Funds:\t", self.__funds_available)
    
    
    def __str__(self):
        """ convert class to string """
    
        return '\nCard PIN:\t' + str(self.__card_pin) + \
               '\nAvailable Funds:\t\t' \
               + str(self.__funds_available)
