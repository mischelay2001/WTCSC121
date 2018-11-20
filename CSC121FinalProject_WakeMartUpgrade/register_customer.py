__author__ = 'Michele Johnson'

""" Register Customer 

The class has six methods:

1.	__init__ – The constructor receives customer name as an argument and stores it in an instance variable.  
It should also create the other instance variables and initialize them all to empty strings.

2.	input_card_info – In this method, the user enters credit card number, 
credit card security code, debit card number and debit card PIN.  
All these input values should be stored in instance variables.

3.	verify_credit_card – This method will check whether the security code is correct.  
This method is called when the user chooses to pay by credit card.  
It compares the security code entered by the user during check out against the security code stored in the 
Customer object.  If they are the same, this method returns True.  Otherwise, it returns False.

4.	verify_debit_card – This method is similar to verify_credit_card.  
It compares the PIN entered by the user during checkout against the PIN stored in the Customer object.  
If they are the same, this method returns True.  Otherwise, it returns False.

5.	credit_card_last_four method returns the last four digits of the credit card number.

6.	debit_card_last_four returns the last four digits of the debit card number.  

This class has five private instance variables to store customer name, credit card number, 
credit card security code, debit card number, and debit card PIN. """

# Import statements
from CSC121FinalProject_WakeMartUpgrade import valid_entry
from CSC121FinalProject_WakeMartUpgrade import formatting


# Define class
class RegisterCustomer:

    """ Creates two protected instance variables to store the user's meat and side choices """

    def __init__(self):
        """ constructor of class MealExpress"""

        self._first_name = ""
        self._last_name = ""
        self._debit_num = ""
        self._pin_num = ""
        self._credit_num = ""
        self._security_code = ""

    def CustomerName(self):

        """ Register customer name; display instruction; welcome message """

        # Heading
        heading_register_customer = "CUSTOMER REGISTRATION"
        formatting.headings(heading_register_customer)

        # Introduce registration
        print("Please register before ordering:\n")

        # Receive customer name
        # check name is alphabetic, clean unwanted characters, title case
        request_text_first = "First Name"
        self._first_name = valid_entry.alpha_entry(request_text_first)

        # check name is alphabetic, clean unwanted characters, title case
        request_text_last = "Last Name"
        self._last_name = valid_entry.alpha_entry(request_text_last)

        # Display name and welcome message
        print("\nWelcome " + self._first_name + " " + self._last_name + "!\n")

    def RegisterCards(self):

        """ Register customer card information for payment """

        # Print Payment Card Registration heading
        heading_payment_register = "PAYMENT CARD REGISTRATION"
        formatting.headings(heading_payment_register)

        # Instructions
        print("Register both a debit card and credit card:")

        # Debit Card
        # user enters debit card number and debit card PIN
        print("\nDebit Card")

        # check number is 16 digits, clean unwanted characters
        request_text_debit = "\tEnter the 16-digit debit card number:\t\t"
        self._debit_num = valid_entry.clean_string_digits(request_text_debit, 16)

        # check number is 4 digits, clean unwanted characters
        request_text_pin = "\tEnter the 4-digit debit card PIN:\t\t\t"
        self._pin_num = valid_entry.clean_string_digits(request_text_pin, 4)

        # Credit Card
        # user enters credit card number, credit card security code
        print("\nCredit Card")

        # check number is 16 digits, clean unwanted characters
        request_text_credit = "\tEnter the 16-digit credit card number:\t\t"
        self._credit_num = valid_entry.clean_string_digits(request_text_credit, 16)

        # check number is 3 digits, clean unwanted characters
        request_text_security = "\tEnter the 3-digit credit card security code:"
        self._security_code = valid_entry.clean_string_digits(request_text_security, 3)

    def GetSecurityCode(self):

        """ Get and return credit card security code """

        return self._security_code

    def GetSecurityPin(self):

        """ Get and return debit card PIN """

        return self._pin_num

    def DisplayRegistration(self):

        """ Display cards on file, confirm registration, thank you message, instruction """

        # Confirm cards on file with last 4 digits
        print("\nCards now on file:")
        print("\tDebit Card\tending in " + self._debit_num[12:16])
        print("\tCredit Card\tending in " + self._credit_num[12:16])

        # Confirm registration is complete
        print("\nRegistration Complete")

        # Thank customer for registering
        print("\nTHANK YOU, " + self._first_name.upper() + "!\n")

        # Instructions
        print("Please proceed with your order:\n")
