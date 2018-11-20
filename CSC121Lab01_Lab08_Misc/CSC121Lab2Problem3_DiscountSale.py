__author__ = 'Michele Johnson'
#Program requirements:
# All jackets in a store are on sale now.  They need a program to process discounts.
# The user will enter the original price of a jacket and the discount percentage using a decimal
# (for example: if it is 25% off, the user should enter 0.25; if it is 30% off, the user should enter 0.30, etc).
# The program will use the original price and the discount percentage entered by the user to calculate the sale price
# (i.e. the reduced price).  It will all calculate sales tax and total amount due.  Use 0.07 as sales tax rate.
# There is no need to ask the user to enter sales tax rates.  Display sale price, sales tax and total amount due.

# Get input from user:
Org_Prc = float(input('Enter the original price of the item on sale:  '))
Pct_Dis = float(input('Enter the discount percentage for the item:  '))

#Calculations
Pct_Dis_100 = Pct_Dis / 100
Disc = Org_Prc * Pct_Dis_100
Sale_Prc = Org_Prc - Disc
Sal_Tx_Amt = Sale_Prc * 0.07
Tot_Amt = Sale_Prc + Sal_Tx_Amt

#Output
print('\nThe original price of your item was $' + (format(Org_Prc, ',.2f')) + '.\n')
print('With ' + (format(Pct_Dis_100, '.0%')) + ' off...')
print('The sale price is $' + (format(Sale_Prc, ',.2f')) + '.')
print('The sales tax is $' + (format(Sal_Tx_Amt, ',.2f')) + '.')
print('\nThis brings the total cost of the item to $' + (format(Tot_Amt, ',.2f')) + ' including tax.')
