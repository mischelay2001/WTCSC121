__author__ = 'Michele Johnson'
# Program Requirements
# A group of high school students are selling pizza and soda during a basketball game to raise fund for a field trip.  
# Pizza is $3.50 per slice and soda is $1.25 per cup.  Design a program to do the following.  
# Ask the user to enter number of cups of soda and number of slices of pizza ordered by the customer.  
# The program will calculate and display the total amount due from the customer.

# Get input from user
Num_Cups = int(input('Enter the number of cups of drink ordered:  '))
Num_Slice = int(input('Enter the number of slices of ordered:  '))

# Calculations
Soda_Prc = Num_Cups * 1.25
Pizza_Prc = Num_Slice * 3.50
Tot_Amt = Soda_Prc + Pizza_Prc

# Output
print('\nDrink total:\t\t$' + (format(Soda_Prc, ',.2f')))
print('Pizza slices total:\t$' + (format(Pizza_Prc, ',.2f')))
print('\nOrder total:\t\t$' + (format(Tot_Amt, ',.2f')))
