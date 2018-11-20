__author__ = 'Michele Johnson'
# Program Requirements
# Residential and business customers are paying different rates for water usage.
# Residential customers pay $0.004 per gallon for the first 8000 gallons.
# If the usage is more than 8000 gallons, the rate will be $0.007 per gallon after the first 8000 gallons.
# Business customers pay $0.005 per gallon for the first 10000 gallons.
# If the usage is more than 10000 gallons, the rate will be $0.009 per gallon after the first 10000 gallons.
# For example, if a business customer has used 12000 gallons,
# they need to pay $50 for the first 10000 gallons ($0.005 * 100000),
# plus $18 for the other 2000 gallons ($0.009 * 2000).  Write a program to do the following.
# Ask the user which type the customer it is and how many gallons of water have been used.
# Calculate and display the bill.

# Introduce the program
print('This program calculates the water bill amounts for both residential and business customers.\n')
print('Residential customers pay $0.004 per gallon for the first 8000 gallons.')
print('If the usage is more than 8000 gallons, the rate will be $0.007 per gallon after the first 8000 gallons.')
print('\nBusiness customers pay $0.005 per gallon for the first 10000 gallons.')
print('If the usage is more than 10000 gallons, the rate will be $0.009 per gallon after the first 10000 gallons.')

# Get customer type input from user
print("\nWill this be for a residential or business customer?")
customer_type = str(input('Please type "R" for residential or "B" for business.  \n'))
customer_type = customer_type.upper()
# Input is made up of only letters; aVariable is alpha - True or False
variable_alpha = False
valid_code = False

# Handle invalid user input
# while REQUIRED INPUT DOES NOT MEET NEEDS is False:
while variable_alpha is False and valid_code is False:
            try:
                variable_alpha = customer_type.isalpha()
                valid_code = customer_type is 'R' or  customer_type is 'B'

            # Except if the user's input breaks the code
            except:
                pass
                print('\nYour entry is invalid.')

# Begin program block
if customer_type == 'R':
    gallons_resident = int(input('\nEnter number of gallons used by the residential customer:  '))
    if gallons_resident >= 8000:
        difference = gallons_resident - 8000
        tier1 = (gallons_resident - difference) * 0.004
        tier2 = difference * 0.007
        bill = tier1 + tier2
        print('\nThe residential water bill is $' + (format(bill, ',.2f')) + '.')
    else:
        bill = gallons_resident * 0.004
        print('\nThe residential water bill is $' + (format(bill, ',.2f')) + '.')

else:
    gallons_business = int(input('\nEnter number of gallons used by the commercial customer:  '))
    if gallons_business >= 10000:
        difference = gallons_business - 10000
        tier1 = (gallons_business - difference) * 0.005
        tier2 = difference * 0.009
        bill = tier1 + tier2
        print('\nThe commercial water bill is $' + (format(bill, ',.2f')) + '.')
    else:
        bill = gallons_business * 0.005
        print('\nThe commercial water bill is $' + (format(bill, ',.2f')) + '.')
