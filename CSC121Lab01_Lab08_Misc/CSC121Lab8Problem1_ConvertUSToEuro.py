__author__ = 'Michele Johnson'
# Program Requirements
# Write a program to convert US dollar to Euro.
# This program has two functions: main and a value-returning function convert_to_euro.
# Please do the following:
#
# (a)	In the main function, ask user to enter amount in US dollar.
# (b)	In the main function, call the convert_to_euro function and pass the amount in US dollar to it.
# (c)	In the convert_to_euro function, write code to convert US dollar to Euro.
# 1 US dollar is equal to 0.88 Euro. Return the amount in Euro.
# (d)	The main function receives and displays the amount in Euro.


# Introduce Program
print("US to Euro Exchange")
print("This program will calculate the exchange from US dollars to Euros.\n")


def main():
    # Main function for US to Euro Exchange program
    # Function will receive a US dollar amount and convert to Euro dollars.
    # Will display the results
    us_dollars = valid_entry()
    euro_dollars = calculate_exchange(us_dollars)
    print('$' + (format(us_dollars, ',.2f')) + ' US dollars exchanges to ' + '$'
          + (format(euro_dollars, ',.2f') + ' Euros.'))


def valid_entry():
    # Function to obtain valid entry per program requirements
    # Will ask user for input as a float for US dollars
    # Will return an error message if entry is invalid
    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value: float; greater than zero
    us_money = 0.0
    while is_entry_valid is False:
        try:
            us_money = float(input("Please enter the amount of US dollars:\t"))
            if us_money > 0:
                is_entry_valid = True
            else:
                print("\nThe entry is not valid.")
                print("Please enter a dollar amount greater than 0.\n")
        except ValueError:
            pass
            print("\nThe entry is not valid.\n")
    return us_money


def calculate_exchange(us_dollars):
    # Function to calculate exchange rate from US dollars to Euros
    # Will return the Euro amount
    euro = us_dollars * 0.88
    return euro


main()
