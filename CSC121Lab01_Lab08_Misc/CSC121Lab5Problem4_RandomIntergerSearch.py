__author__ = 'Michele Johnson'
# Program Requirements

# Write a Python program to do the following:
# (a)	Ask the user to enter 6 integers.  Store them in a list.  Display the list.
# (b)	Select elements that are larger than 20.
# Copy these elements to another list.  Display that list.

# Introduce program

print('This program requests integers to form a list.  '
      '\nValues in the list that meet program criteria will be copied to another list. \n')

# Declare Variables

list_len = 6
list_filter = 20
list_a = []
list_b = []
element_count = 0
filter_count = 0

# Get input from user

print(list_len, 'numbers are needed for the list:\t\t\t\n')
while element_count < list_len:
    user_number = int(input('Enter an integer:\t\t'))
    list_a.append(user_number)
    element_count = element_count + 1
print('\nThank you!\n'
      'Values greater than', list_filter, 'will be added to a new list.')

# Filter to new list

element_count = 0
while element_count < list_len:
    if list_a[element_count] > list_filter:
        list_b.append(list_a[element_count])
    element_count = element_count + 1

if list_b != []:
    list_len = len(list_b)
    list_b.sort()
    print('\nThe following values were greater than', list_filter,
          'and have been added to a second list:')
    element_count = 0
    while element_count < list_len:
        print(list_b[element_count])
        element_count = element_count + 1
else:
    print('\nNone of the ', list_len, ' values entered were greater than ', list_filter, '.', sep='')
