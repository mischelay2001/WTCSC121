__author__ = 'Michele Johnson'
# Program Requirements

# Write a program to calculate tuition for students of a community college.
# In-state students pay $60 per credit hour, and will pay for only
# 12 credit hours even if they register for more hours.
# Out-of-state students pay $200 per credit hour, and will pay for
# 15 credit hours as the maximum.
# In the main function, ask the user whether he is in-state or out-of-state.
# Then ask the user how many credit hours he is taking.
# Call one of these two functions to calculate tuition.


def main():
    print('This program will calculate in-state or out-of-state tuition for students of a community college.\n')
    print('Enter 1 if you are in-state student.')
    print('Enter 2 if you are an out-of-state student.\n')
    instate = int(input('Please enter 1 or 2 per the instructions above.\t\t'))
    credit_hours = float(input('Please the number of credit hours taken.\t\t\t'))
    print()
    if instate == 1 or instate == 2:
        if instate == 1:
            instate_tuition(credit_hours)
        elif instate == 2:
            out_of_state_tuition(credit_hours)
    else:
        print('You did not select a valid option.')


def instate_tuition(hours):
    if hours < 12:
        tuition = 60 * hours
    else:
        tuition = 60 * 12
    print('Your in-state tuition is $' + (format(tuition, ',.2f')) + '.')


def out_of_state_tuition(hours):
    if hours < 15:
        tuition = 200 * hours
    else:
        tuition = 200 * 15
    print('Your out-of-state tuition is $' + (format(tuition, ',.2f')) + '.')


main()
