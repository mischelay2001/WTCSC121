__author__ = 'Michele Johnson'
# Program Requirements

# A real estate agent earns 3% commission for every house he sells.
# Write a Python program to do the following:
# (a)	Ask the user to enter the number of houses the real estate agent has sold.
# (b)	Use a for loop to get the prices of the houses.  Store the prices in a list.
# (c)	Use a for loop to display price and commission earned for each house.

# Introduce program
print('This program will capture a real estate agent\'s commission for each house sold.\n')

# Declare Variables
num_sold = 0
price = 0
price_total = []
commission = 0
commission_total = []
house_num = []
i = 0

# Get input from user
num_sold = int(input('How many houses have been sold?\t\t\t\t'))

# Calculations
for i in range(num_sold):
    price = float(input('What was the sale price?\t\t\t\t\t'))
    price_total.append(price)
    commission = price * 0.03
    commission_total.append(commission)
    i = i + 1
    house_num.append(i)

# Output
for j in range(len(house_num)):
    print('House',house_num[j],': $' + format(commission_total[j], ',.2f'),
          'was earned on $' + (format(price_total[j], ',.2f')))
    j = j + 1

