__author__ = 'Michele Johnson'
# Program Requirements
# A high school senior is applying for colleges.  He wants a program to calculate the out-of-pocket cost
# for attending each college he is applying.  The out-of-pocket cost is determined by the following formula:
#
# 	out-of-pocket cost = tuition + room + board + other expenses – financial aid
#
# Write a program to calculate the out-of-pocket cost of every college he is applying.
# After each college, ask the user whether to calculate cost for another college.  Enter ‘y’ for yes.

# Introduce program
print('This program will calculate the out-of-pocket cost for each college you have applied for.\n')

# Declare Variables

count = 0
college = ''
college_num = ''
tuition = ''
room = ''
board = ''
other = ''
aid = ''
out_of_pocket = ''

raw_input_valid = False
while raw_input_valid is False:
    try:
        college_num = int(input('How many colleges have you applied for admission?\t\t\t\t'))
        if college_num > 0:
            raw_input_valid = True
            print("\nGreat!"
                  "\nNow let's calculate the out-of-pocket for each college.")
            print('\nPlease enter the following:\n')
        else:
            print('\nCollege is an important part of your future.'
                  '\nYou should apply to some schools.'
                  '\nIt can be more affordable than you might think.\n')
    except ValueError:
        print('\nInvalid Entry'
              '\nThe number of colleges applied for admission must be greater than 0.'
              '\nPlease enter a valid number.\n')

while count < college_num:
    count = count + 1
    raw_input_valid = False
    while raw_input_valid is False:
        try:
            college = str(input('What is the name of the college?\t\t\t\t\t\t\t\t'))
            tuition = float(input('How much is the college tuition?\t\t\t\t\t\t\t\t'))
            if tuition >= 0:
                raw_input_valid = True
            else:
                print('\nInvalid Entry'
                      '\nThe expense amount must be greater than or equal to 0.'
                      '\nPlease enter a valid amount.\n')
        except ValueError:
            print('\nInvalid Entry'
                  '\nThe tuition amount must be greater than or equal to 0.'
                  '\nPlease enter a valid amount.\n')
    raw_input_valid = False
    while raw_input_valid is False:
        try:
            room = float(input('How much is the room expense?\t\t\t\t\t\t\t\t\t'))
            if room >= 0:
                raw_input_valid = True
            else:
                print('\nInvalid Entry'
                      '\nThe expense amount must be greater than or equal to 0.'
                      '\nPlease enter a valid amount.\n')
        except ValueError:
            print('\nInvalid Entry'
                  '\nThe room amount must be greater than or equal to 0.'
                  '\nPlease enter a valid amount.\n')
    raw_input_valid = False
    while raw_input_valid is False:
        try:
            board = float(input('How much is the board expense?\t\t\t\t\t\t\t\t\t'))
            if board >= 0:
                raw_input_valid = True
            else:
                print('\nInvalid Entry'
                      '\nThe expense amount must be greater than or equal to 0.'
                      '\nPlease enter a valid amount.\n')
        except ValueError:
            print('\nInvalid Entry'
                  '\nThe board amount must be greater than or equal to 0.'
                  '\nPlease enter a valid amount.\n')
    raw_input_valid = False
    while raw_input_valid is False:
        try:
            other = float(input('If there will be other expenses, enter the amount here:\t\t\t'))
            if other >= 0:
                raw_input_valid = True
            else:
                print('\nInvalid Entry'
                      '\nThe expense amount must be greater than or equal to 0.'
                      '\nPlease enter a valid amount.\n')
        except ValueError:
            print('\nInvalid Entry'
                  '\nThe other expenses must be greater than or equal to 0.'
                  '\nPlease enter a valid amount.\n')
    raw_input_valid = False
    while raw_input_valid is False:
        try:
            aid = float(input('If college has awarded financial aid, enter the amount here:\t'))
            if aid >= 0:
                raw_input_valid = True
            else:
                print('\nInvalid Entry'
                      '\nThe expense amount must be greater than or equal to 0.'
                      '\nPlease enter a valid amount.\n')
        except ValueError:
            print('\nInvalid Entry'
                  '\nThe financial aid amount must be greater than or equal to 0.'
                  '\nPlease enter a valid amount.\n')

    # Calculations
    out_of_pocket = tuition + room + board + other - aid

    # Output
    print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThe out-of-pocket cost for', college,
          'is $' + (format(out_of_pocket, ',.2f') + '.\n'))

    if count < college_num:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tNow let's look at the next college...\n")
    else:
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThat was the last college.')
