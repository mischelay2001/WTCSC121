__author__ = 'Michele Johnson'
# Program requirements:
# The program asks the user to enter the room’s length, width and height,
# and uses the following formula to calculate the number of btu needed:
# btu needed = room volume * 3.5
# Now we want to add one more consideration.
# If the room gets a lot of sunlight, number of btu needed will increase by 20%.
# The program needs to ask the user whether the room gets a lot of sunlight.
# The user answers ‘yes’ or ‘no’.  Adjust the number of btu needed if necessary.

# Introduce the program
print("This program will determine the air conditioner capacity in btu's required to cool a room." 
      "\nIt will make adjustments for rooms with extra sunlight.\n")
print('Please enter the following room dimensions...\n')

# Get initial dimension input from user
length = input('Enter length of the room in feet: ')
width = input('Enter width of the room in feet: ')
height = input('Enter height of the room in feet: ')
boolean_valid_dimension = False

# Validate if dimension input are floats
while boolean_valid_dimension is False:
    try:
        length = float(length)
        width = float(width)
        height = float(height)
        boolean_valid_dimension = (float(length) >= 0) and (float(width) >= 0) and (float(height) >= 0)
    except:
        pass
        print('\nInvalid entry.  Please re-enter each room dimension as a number...\n')
        # Re-ask for valid input
        length = input('Enter length of the room in feet: ')
        width = input('Enter width of the room in feet: ')
        height = input('Enter height of the room in feet: ')
        boolean_valid_dimension = (float(length) >= 0) and (float(width) >= 0) and (float(height) >= 0)

# Get initial sunlight input from user
extra_sunlight = int(input('\nDoes the room have extra sunlight?  Please type "1" for YES or "2" for NO. '))
Boolean_Valid_Entry_Sun = extra_sunlight is 1 or extra_sunlight is 2

# Validate if sunlight input is 1 or 2
while Boolean_Valid_Entry_Sun is False:
    print('Invalid entry.  Please type "1" for YES or "2" for NO.')
    # Re-ask for valid input
    extra_sunlight = int(input('\nDoes the room have extra sunlight?  Please type "1" for YES or "2" for NO. '))
    Boolean_Valid_Entry_Sun = extra_sunlight is 1 or extra_sunlight is 2

# Calculations
btu = (float(length)) * (float(width)) * (float(height)) * 3.5
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
