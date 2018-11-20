__author__ = 'Michele Johnson'

""" (a)	Create a Card class.  This class has two private instance variables: id and name.  
The __init__ method takes card number and customer name as two arguments and stores them in the instance variables. 
Define a displayIdName method to display id and name.  Define two abstract methods inputInfo and displayInfo.  
These abstract methods have no real code.  There is only one statement to raise a NotImplementedError exception. """


class CardUser:
    """ Creates instance variables """

    def __init__(self, card_number, card_user):
        """ constructor """

        self.__card_number = card_number
        self.__card_user = card_user

    def displayIdName(self):
        print("Card Number:\t", self.__card_number)
        print("Card User:\t", self.__card_user)


    def inputInfo(self):
        raise NotImplementedError("Method inputStat not implemented")


    def displayInfo(self):
        raise NotImplementedError("Method displayStat not implemented")


    def __str__(self):
        """ convert class to string """

        return '\nCard Number:\t' + str(self.__card_number) + \
               '\nCard User:\t\t' \
               + str(self.__card_user)
