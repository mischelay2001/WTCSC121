__author__ = 'Michele Johnson'

"""  5.	make_payment

The make_payment function has two parameters to receive the 
Customer object and the total amount to pay.  It asks the customer to choose a payment method.  
If the user chooses to pay by credit card, ask the user to enter the security code.  
Call the verify_credit_card method of the Customer object to verify the security code.  
If the security code is incorrect, display “Security code incorrect. Payment rejected.” 
and loop back to ask the customer to choose payment method again.  If the security code is correct, 
display on the screen the amount to be charged and the last four digits of the credit card number. 

If the user chooses to pay by debit card, ask the user to enter the PIN.  
Call the verify_debit_card method of the Customer object to verify the PIN.  
If the PIN is incorrect, display “PIN incorrect. Payment rejected.” 
and loop back to ask the customer to choose payment method again.  
If PIN is correct, display on the screen the amount to be charged and the last four digits of the debit card number. """

# Import Statements
from CSC121FinalProject_WakeMartUpgrade import valid_entry
from CSC121FinalProject_WakeMartUpgrade import formatting


def payment_choice():
    """ This function allows the user to choose payment type [1 for debit card, 2 for credit card]. """

    # Print Payment Method heading
    payment_method_heading = "PAYMENT METHOD"
    formatting.headings(payment_method_heading)
    print("The self-checkout machine only accepts Debit or Credit Cards.\n")

    # Valid payment choice; returns choice as integer
    def entry_card_choice():
        """ gets valid menu choice """

        a_choice = 0
        is_valid = False
        while is_valid is False:
            print("Payment Method Choices:\n"
                  "\t 1 for Debit Card\n"
                  "\t 2 for Credit Card\n")
            request_text = "Please specify the card for payment"
            a_choice = valid_entry.integer_entry(request_text)

            if a_choice < 1 or a_choice > 2:
                print("\nNot a valid selection.\n"
                      "Please try again.\n")
            else:
                is_valid = True

        return a_choice

    payment_choice = entry_card_choice()

    return payment_choice


def payment_debit(a_balance, a_pin):
    """ This function receives debit payment.
        It also asks customer to enter payment amount.
        Use a validation loop to ensure that payment is not lower than balance.
        If payment is higher than balance, calculate and display cash back amount."""

    # Initiate Variables
    cash_back = 0.0
    is_match = False
    is_valid_payment = False
    check_pin = -1

    print()
    heading_debit_payment = "DEBIT CARD PAYMENT"
    formatting.headings(heading_debit_payment)

    print("For the card on file:")

    # Security Check
    # Pass PIN to verify with user entry
    while is_match is False:
        request_text = "\tEnter the 4-digit debit card PIN:\t\t\t"
        check_pin = valid_entry.clean_string_digits(request_text, 4)
        # Compare entry against pin on file
        if check_pin != a_pin:
            print("\n\tThe PIN entered does not match what is on file.\n")
        if check_pin == a_pin:
            is_match = True

    print('\nTOTAL ORDER..........$' + (format(a_balance, ',.2f')))

    # loop until payment amount is valid
    while is_valid_payment is False:
        # Obtain amount customer authorizes for debit card payment
        request_payment_amount = "\n\tEnter the payment amount"
        payment_amount = valid_entry.float_entry(request_payment_amount)

        if payment_amount >= a_balance:
            cash_back = payment_amount - a_balance
            print("\nYour Debit Card has been processed!\n")
            print('\tCASH BACK.......$' + (format(cash_back, ',.2f')))
            is_valid_payment = True
        else:
            print('\n\tThe payment must be greater than or equal to the balance: $' + (format(a_balance, ',.2f')))


def payment_credit(a_balance, a_code):
    """ This function receives credit payment.
        It also asks customer to enter payment amount.
        Use a validation loop to ensure that payment is not lower than balance.
        If payment is higher than balance, calculate and display cash back amount."""

    # Initiate Variables
    is_match = False
    check_code = -1

    print()
    heading_credit_payment = "CREDIT CARD PAYMENT"
    formatting.headings(heading_credit_payment)

    print("For the card on file:")

    # Security Check
    # Pass PIN to verify with user entry
    while is_match is False:
        request_text = "\n\tEnter the 3-digit credit card security code:"
        check_code = valid_entry.clean_string_digits(request_text, 3)
        # Compare entry against pin on file
        if check_code != a_code:
            print("\n\tThe security code entered does not match what is on file.\n")
        if check_code == a_code:
            is_match = True

    print('\nTOTAL ORDER..........$' + (format(a_balance, ',.2f')))
    print('\nYour Credit Card ending in ' + a_code + ' has been processed for $'
          + (format(a_balance, ',.2f')) + '.\n')
