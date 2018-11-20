__author__ = 'Michele Johnson'
# Program Requirements
# A company gives volume discount to customers of their software product.
# Unit price depends on number of copies purchased:
#
# Number of copies purchased	Unit price
# 1 - 10                        $99
# 11 - 50                       $89
# 51 - 100                      $79
# 101 or more                   $69
#
# Write a program to do the following.  Ask the customer how many copies he is buying.
# Display the unit price.  Calculate and display total price.

# Introduce program
print('Volume Discount')
print('\nThis program will calculate the unit and total prices dependent on number of copies purchased.\n')
print('Number of copies purchased\t\t\t\t\tUnit Price')
print('1 - 10\t\t\t\t\t\t\t\t\t\t$99')
print('11 - 50\t\t\t\t\t\t\t\t\t\t$89')
print('51 - 100\t\t\t\t\t\t\t\t\t$79')
print('101 or more\t\t\t\t\t\t\t\t\t$69\n')

# Get number of copies input from user
copies = str(input('How many copies are you buying?  '))
boolean_copies_numeric = False

# Validate copies input
while boolean_copies_numeric is False:
    try:
        boolean_copies_numeric = copies.isnumeric()

        #Begin program comparison
        copies = int(copies)
        if copies <=10:
            unit_price = 99
            total_price = unit_price * copies
        elif copies >10 and copies <=50:
            unit_price = 89
            total_price = unit_price * copies
        elif copies >51 and copies <=100:
            unit_price = 79
            total_price = unit_price * copies
        else:
            unit_price = 69
            total_price = unit_price * copies

        #Output
        print('\nThe unit price is $' + format(unit_price, ',.0f') +
              ' per copy.  The total price is $' + format(total_price, ',.0f') +
              ' for ' + format(copies, ',.0f') + ' copies.')

    except ValueError:
        pass
        print('\nYour entry is invalid.  Please select a valid code from the table above.')
        copies = input('\nPlease enter the number of copies you are buying:  ')

