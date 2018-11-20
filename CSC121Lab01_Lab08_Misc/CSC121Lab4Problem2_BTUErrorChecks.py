__author__ = 'Michele Johnson'
# Program requirements:
# The program asks the user to enter the room’s length, width and height,
# and uses the following formula to calculate the number of btu needed:
# btu needed = room volume * 3.5
# Now we want to add one more consideration.
# If the room gets a lot of sunlight, number of btu needed will increase by 20%.
# The program needs to ask the user whether the room gets a lot of sunlight.
# The user answers ‘yes’ or ‘no’.  Adjust the number of btu needed if necessary.
# Modify the program from Lab3Problem 2by adding error checking loops.
# Room length, width and height must all be greater than 0.
# Every time the user enters a negative number, display an error message
# and ask the user to re-enter a valid value immediately.

# Introduce the program
print("This program will determine the air conditioner capacity in btu's required to cool a room." 
      "\nIt will make adjustments for rooms with extra sunlight.\n")
print('Please enter the following room dimensions...\n')

# Declare Variables
length = ''
width = ''
height = ''
extra_sunlight = ''

# Validate if dimension input are floats
boolean_valid_dimension = False
while boolean_valid_dimension is False:
    try:
        length = float(input('Enter length of the room in feet: '))
        if length > 0:
            boolean_valid_dimension = True
        else:
            print('\nInvalid entry.  Please re-enter room dimension as a number...\n')
    except ValueError:
        print('\nInvalid entry.  Please re-enter room dimension as a number...\n')

boolean_valid_dimension = False
while boolean_valid_dimension is False:
    try:
        width = float(input('Enter width of the room in feet: '))
        if width > 0:
            boolean_valid_dimension = True
        else:
            print('\nInvalid entry.  Please re-enter room dimension as a number...\n')
    except ValueError:
        print('\nInvalid entry.  Please re-enter room dimension as a number...\n')

boolean_valid_dimension = False
while boolean_valid_dimension is False:
    try:
        height = float(input('Enter height of the room in feet: '))
        if height > 0:
            boolean_valid_dimension = True
        else:
            print('\nInvalid entry.  Please re-enter room dimension as a number...\n')
    except ValueError:
        print('\nInvalid entry.  Please re-enter room dimension as a number...\n')

boolean_valid_entry_sun = False
while boolean_valid_entry_sun is False:
    try:
        extra_sunlight = int(input('\nDoes the room have extra sunlight?  Please type "1" for YES or "2" for NO. '))
        if extra_sunlight is 1 or extra_sunlight is 2:
            boolean_valid_entry_sun = True
            pass
        else:
            print('Invalid entry.  Please type "1" for YES or "2" for NO.')
    except ValueError:
        print('Invalid entry.  Please type "1" for YES or "2" for NO.')

# Calculations
btu = length * width * height * 3.5
need_btu = btu + (btu * 0.20)

# Output
# There is extra sunlight
if extra_sunlight is 1:
    print('\nYou have indicated there is extra sunlight in the specified room.')
    print('A ' + format(need_btu, ',.0f') + ' BTU capacity air conditioner would be required to cool this room.')
# There is no extra sunlight
else:
    print('\nSince the room does not receive extra sunlight, a ' + format(btu, ',.0f') +
          ' BTU capacity air conditioner would be sufficient to cool this room.')
