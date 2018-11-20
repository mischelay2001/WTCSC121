__author__ = 'Michele Johnson'
# Program Requirements

# Write a Python program to do the following:
# (a)	Use the range function to generate this sequence of integers: 2, 3, 4, 5.
# Save the sequence in a list.
# (b)	Use the range function to generate this sequence of integers: 2, 5, 8, 11.
# Save the sequence in a list.
# (c)	Use the range function to generate this sequence of integers: 9, 7, 5, 3.
# Save the sequence in a list.
# (d)	Concatenate the three lists created in parts (a), (b) and (c) into a one list.
# Write a for loop to display each element of the combined list in a separate line.


# Introduce program
print('This program utilizes the range function on lists.\n')

# Declare Variables
list1 = []
list2 = []
list3 = []
all_lists = []

# Calculations
for x in range(2,6,1):
    list1.append(x)
    all_lists.append(x)
for x in range(2,12,3):
    list2.append(x)
    all_lists.append(x)
for x in range(9,2,-2):
    list3.append(x)
    all_lists.append(x)

# Output
print(list1)
print(list2)
print(list3)
print(all_lists)
for x in range(len(all_lists)):
    print(all_lists[x])
