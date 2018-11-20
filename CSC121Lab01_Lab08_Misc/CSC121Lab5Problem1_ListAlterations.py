__author__ = 'Michele Johnson'
# Program Requirements
# Write a Python program to do the following:
# (a)	Create a list to store the following values: 4, 1, 7 and 6.  Display the list.
# (b)	Change the second element from 1 to 2.  Display the modified list.
# (c)	Change the last element from 6 to 5.  You must use negative index.
#       Display the modified list.
# (d)	Add a new element 8 to the end of the list.  Display the modified list.
# (e)	Add a new element 9 as the new first element of the list.
#       Display the modified list.

# Introduce program
print('This program will create a list and alter the list elements.\n')

# Output

# Create a List
values = [4,1,7,6]
print('The list "values" has been created and contains the following values:'
      '\t\t', values)

# Change the second list element
values[1] = 2
print('The second list element has been changed from 1 to 2:'
      '\t\t\t\t\t\t', values)

# Change the last list element via negative index
values[-1] = 5
print('The last list element has been changed from 6 to 5:'
      '\t\t\t\t\t\t\t', values)

# Appending new value as the last list element
values.append(8)
print('8 has been added as the last element to the list:'
      '\t\t\t\t\t\t\t', values)

# Insert new value as the first list element
values.insert(0,9)
print('9 has been inserted as the first element to the list:'
      '\t\t\t\t\t\t', values)

