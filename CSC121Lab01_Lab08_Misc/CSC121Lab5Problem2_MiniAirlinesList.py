__author__ = 'Michele Johnson'
# Program Requirements

# Mini Airlines needs a program to create passenger lists.
# Write a program to do the following:
# (a)	Enter the number of passengers
# (b)	Enter the names of the passengers.  Store the names in a list.
# (c)	Display the passenger list.
# (d)	Sort the passenger list.  Display the sorted list.
# (e)	Ask the user to enter a name.  Search the list to see whether this
#       name is in the list.
#       Display the search result.
# (f)	We need to remove a passenger from the list.
#       Ask the user to enter the name of the passenger to be removed.
#       Remove the passenger.  Display the list.
# (g)	Use the len function to find the length of the list.  Display the length.

# Introduce program
print('This program will create a passenger list for Mini Airlines.\n'
      'The list will be manipulated as specified by the program requirements.\n')

# Declare Variables

names_raw_entry = ''
names_passengers = []
name_count = 0
name_search = ''

# Get input from user
num_passengers = int(input('Please enter the number of passengers to be listed:\t\t'))
print('\nGreat!\n'
      'Now let\'s get the passenger names:\n')

while name_count < num_passengers:
    names_raw_entry = str(input('Please enter a passenger name:\t\t\t\t\t\t\t'))
    names_raw_entry = names_raw_entry.title()
    names_raw_entry = names_raw_entry.strip()
    names_passengers.append(names_raw_entry)
    name_count = name_count + 1

# Output
print('\nHere\'s the list of names entered:'
      '\t\t\t\t\t\t', names_passengers)
names_passengers.sort()
print('\nHere\'s the list sorted to make it easier to read:'
      '\t\t', names_passengers)

# Search the list
names_raw_entry = input('\nTo search the list for a specific name.'
                        '\nPlease enter the name to search:\t\t\t\t\t\t')
names_raw_entry = names_raw_entry.title()
names_raw_entry = names_raw_entry.strip()
if names_raw_entry in names_passengers:
    print('')
    print(names_raw_entry, 'was found in the list.')
else:
    print('')
    print(names_raw_entry, 'was not found in the list.')

# Delete from the list
names_raw_entry = input('\nTo delete a specific name from the list.'
                        '\nPlease enter the name to be deleted:\t\t\t\t\t')
names_raw_entry = names_raw_entry.title()
names_raw_entry = names_raw_entry.strip()
if names_raw_entry in names_passengers:
    names_passengers.remove(names_raw_entry)
    print('')
    print(names_raw_entry, 'was found in the list and has been deleted.')
else:
    print('')
    print(names_raw_entry, 'was not found in the list.')

# Determine the number of names in the list
num_passengers = len(names_passengers)
print('\nHere\'s the list of name(s) remaining in the list:\t\t', names_passengers)
print('There are', num_passengers, 'remaining in the list.')
