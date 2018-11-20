__author__ = 'Michele Johnson'

""" Program requirements:

A bank issues two types of cards to customers: credit cards and debit cards.  
Both types of cards have a card number and a name.  Credit cards have interest rate and credit limit.  
Debit cards have PIN code and fund available to use.

Write a Python program to manage cards.  Your project must follow these requirements.

(a)	Create a Card class.  This class has two private instance variables: id and name.  
The __init__ method takes card number and customer name as two arguments and stores them in the instance variables. 
Define a displayIdName method to display id and name.  Define two abstract methods inputInfo and displayInfo.  
These abstract methods have no real code.  There is only one statement to raise a NotImplementedError exception.

(b)	Create a CreditCard class.  This class is a derived class of the Card class. 
It has two additional private instance variables: interest_rate and credit_limit.  
Define an inputInfo method to input interest rate and credit limit, and a displayInfo method to display these two items.

(c)	Create a DebitCard class.  This class is a derived class of the Card class. 
It has two additional private instance variables: pin and fund_available.  
Define an inputInfo method to input PIN code and fund available to use, and a  
displayInfo method to display these two items.

(d)	In the main module, ask user to enter name and card number.  
Ask the user whether it is a credit card or debit card.  
Create an object and call its inputInfo method to input information.  
Call the displayIdName method to display card number and name, 
and the displayInfo method to display other information. """

from card import CardUser
from credit_card import CreditCard
from debitcard import DebitCard

def main():

    # Get user input
    card_num = input("Enter card number:\t\t")
    card_user = input("Enter card user's name:\t")

    a_user = CardUser(card_num, card_user)
    print(a_user)

    card_type = int(input("\nEnter 1 for debit or 2 for credit card\t"))
    if card_type == 1:
        debit_info = DebitCard.inputInfo(a_user)
        print()
        display_debit = DebitCard.displayInfo(a_user)
        print()
    if card_type == 2:
        credit_info = CreditCard.inputInfo(a_user)
        print()
        display_credit = CreditCard.displayInfo(a_user)
        print()


main()
