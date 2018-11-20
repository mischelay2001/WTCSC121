__author__ = 'Michele Johnson'
# Program Requirements

# Write a Python program to do the following:
# (a)	Create a list named list1 to store this sequence of numbers: 4, 7, 5, 8, 1, 2, 6, 3.
# (b)	Create a list named list2.  Copy all elements of list1 to list2.
# Display list2.
# (c)	Create a list named list3.  Copy the first 4 elements of list1 to list3.
# Display list3.
# (d)	Create a list named list4.  Copy the last 4 elements of list1 to list4.
# Display list4.

# Introduce program
print('This program copies list elements to create new lists.\n')

# Declare Variables
list1 = [4, 7, 5, 8, 1, 2, 6, 3]
list2 = []
list3 = []
list4 = []
all_lists = []

# Calculations
list2 = list1
print(list2)
for x in range(0,4,1):
    list3.append(list1[x])
    print(list3)
y = len(list1) -1
while y > 3:
    list4.append(list1[y])
    y = y - 1
print(list4)

#
# # Output
# print(list2)
# print(list2)
# print(list3)
# print(all_lists)
# for x in range(len(all_lists)):
#     print(all_lists[x])
