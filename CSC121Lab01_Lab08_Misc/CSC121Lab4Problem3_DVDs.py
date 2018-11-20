__author__ = 'Michele Johnson'
# Program Requirements
# An online store is selling DVDs for $4.99 each.  The buyer pays a shipping and handling fee of $2.99 
# for the whole order.  Write a program to calculate the bill for multiple customers.  
# First ask the user to enter the number of customers.  Then for each customer, enter the number of DVDs purchased.  
# Calculate and display the bill for each customer. 

# Introduce program
print('This program will calculate the DVD bill for customers.\n')

# Declare Variables
count = 0
customer = ''
customer_num = ''
dvd = ''
dvd_cost = 4.99
shipping = 2.99
bill = 0

raw_input_valid = False
while raw_input_valid is False:
    try:
        customer_num = int(input('How many customers would you like to calculate bills for?\t\t'))
        if customer_num > 0:
            raw_input_valid = True
            print("\nGreat!"
                  "\nNow let's calculate the bill for each customer.\n")
#            print('\nRun the program again when you have bills needed to generate for customers.\n')
        else:
            print("\nInvalid Entry"
                  "\nThe number of customers must be greater than 0."
                  "\nPlease enter a valid number.\n")
    except ValueError:
        print('\nInvalid Entry'
              '\nThe number of customers must be greater than 0.'
              '\nPlease enter a valid number.\n')

while count < customer_num:
    count = count + 1
    raw_input_valid = False
    while raw_input_valid is False:
        try:
            customer = str(input('What is the name of the customer?\t\t\t\t\t\t\t\t'))
            dvd = int(input("Enter the number of DVD's ordered?\t\t\t\t\t\t\t\t"))
            if dvd > 0:
                raw_input_valid = True
            else:
                print('\nInvalid Entry'
                      '\nThe amount must be greater than or equal to 0.'
                      '\nPlease enter a valid amount of DVDs.\n')
        except ValueError:
            print('\nInvalid Entry'
                  '\nThe dvd amount must be greater than or equal to 0.'
                  '\nPlease enter a valid amount of DVDs.\n')

    # Calculations
    bill = (dvd * dvd_cost) + (shipping * dvd)

    # Output
    print('\nThe bill for', customer, 'is $' + (format(bill, ',.2f') + '.\n'))

    if count < customer_num:
        print("Now let's look at the next customer...\n")
    else:
        print('That was the last customer.')
