__author__ = 'Michele Johnson'

"""  (b)	Create a CreditCard class.  This class is a derived class of the Card class. 
It has two additional private instance variables: interest_rate and credit_limit.  
Define an inputInfo method to input interest rate and credit limit, 
and a displayInfo method to display these two items. """

from card import CardUser


class CreditCard(CardUser):
    """ Creates instance variables """

    def __init__(self, card_number, card_user):
        base = super()
        base.__init__(self, card_number, card_user)

        """ constructor"""

        self.__interest_rate = 0.0
        self.__credit_limit = 0.0


    def inputInfo(self):
        self.__interest_rate = float(input("Enter interest rate\t"))
        self.__credit_limit = float(input("Enter credit limit\t"))


    def displayInfo(self):
        print("Interest Rate:\t", self.__interest_rate)
        print("Credit Limit:\t", self.__credit_limit)


    def __str__(self):
        """ convert class to string """

        return '\nInterest Rate:\t' + str(self.__interest_rate) + \
               '\nCredit Limit:\t\t' \
               + str(self.__credit_limit)
