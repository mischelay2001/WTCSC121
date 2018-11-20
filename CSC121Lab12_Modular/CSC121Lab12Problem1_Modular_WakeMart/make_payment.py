from CSC121Lab12_Modular.CSC121Lab12Problem1_Modular_WakeMart import valid_entry


def payment_type(a_balance):
    """ This function allows the user to choose payment type [1 for cash, 2 for debit].
        It receives balance as argument, and pass it to pay_cash and pay_debit. """

    print("\nPayment Method\n\n"
          "The self-checkout machine only accepts Cash and Debit Cards.")

    # initialize variables
    valid_choice = False
    choice = ""
    print("Please specify the payment type")
    while valid_choice is False:
        # get valid payment choice from user
        request_pay_type = "\tEnter 1 for cash or 2 for debit"
        pay_type = valid_entry.integer_entry(request_pay_type)
        if pay_type == 1:
            choice = "Cash"
            valid_choice = True
        elif pay_type == 2:
            choice = "Debit"
            valid_choice = True
        else:
            print("Valid entry must be either 1 or 2.")

    return a_balance, choice


def payment_cash(a_balance):
    """ This function receives cash payment.  The self-checkout machine only accepts $10, $5 and $1 bills.
        Ask the user how many $10, $5 and $1 bills he is going to use.  Calculate and display total payment.
        If customer has paid more than the balance, calculate and display change."""

    print("\nCash Payment\n\n"
          "The self-checkout machine only accepts $10, $5 and $1 bills.")

    # Initiate variables
    cash_difference = 0
    payment_enough = False
    cash_count = 0.0

    # loop until customer pays enough cash
    while payment_enough is False:
        # Capture bills for payment
        request_num_of_10 = "\tEnter the number of $10 bills"
        num_of_10 = valid_entry.integer_entry(request_num_of_10)
        request_num_of_5 = "\tEnter the number of $5 bills"
        num_of_5 = valid_entry.integer_entry(request_num_of_5)
        request_num_of_1 = "\tEnter the number of $1 bills"
        num_of_1 = valid_entry.integer_entry(request_num_of_1)

        # calculate cash payment
        total_cash = (num_of_10 * 10) + (num_of_5 * 5) + (num_of_1 * 1)
        cash_count += total_cash
        if cash_count >= a_balance:
            # calculate the amount cash over the balance
            cash_difference = cash_count - a_balance
            payment_enough = True
        elif cash_count < a_balance:
            # loop back to ask for more bills as customer has not paid enough
            cash_difference = a_balance - cash_count
            print('Please pay the remaining balance: $' + (format(cash_difference, ',.2f')))

    return cash_count, cash_difference


def payment_debit(a_balance):
    """This function receives debit payment.
        It asks customer to enter a 16-digit card number and a 4-digit PIN.
        It also asks customer to enter payment amount.
        Use a validation loop to ensure that payment is not lower than balance.
        If payment is higher than balance, calculate and display cash back amount."""

    print("\nDebit Card Payment\n\n"
          "The self-checkout machine accepts Debit Cards with Visa and Mastercard logos.")

    # Initiate Variables
    balance = a_balance
    cash_back = 0.0
    is_valid_payment = False

    # Obtain, clean, display 16-digit credit card number
    request_card_num = "\tEnter the 16-digit debit card number"
    card_length = 16
    card_num = valid_entry.clean_string_digits(request_card_num, card_length)
    print("Card number entered:\t", card_num)

    # Obtain, clean, display 4-digit pin number
    request_pin_num = "\tEnter the 4-digit pin number"
    pin_length = 4
    pin_num = valid_entry.clean_string_digits(request_pin_num, pin_length)
    print("Pin number entered:\t", pin_num)

    # Obtain amount customer authorizes for debt card payment
    request_payment_amount = "\tEnter the payment amount"
    payment_amount = valid_entry.float_entry(request_payment_amount)

    # loop until payment amount is valid
    while is_valid_payment is False:
        if payment_amount >= balance:
            cash_back = payment_amount - balance
            print('Cash back: $' + (format(cash_back, ',.2f')))
            is_valid_payment = True
        else:
            print('The payment must be greater than or equal to the balance: $' + (format(balance, ',.2f')))

    return payment_amount, cash_back
