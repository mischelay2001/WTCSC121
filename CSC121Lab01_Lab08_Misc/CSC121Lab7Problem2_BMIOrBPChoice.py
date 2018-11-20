__author__ = 'Michele Johnson'
# Program Requirements

# Some users of the program in Problem 01 do not want to do both health tests.
# Rewrite the program so the user can choose one of the following:
# (1)	Calculate BMI only
# (2)	Determine high blood pressure only
# (3)	Do both
#
# Your program should continue to have three functions.
# Do not make any changes to the calc_bmi and hypertension functions.
# In the main function, display the options to the user and ask the user to choose.
# Invoke the proper function(s) based on the user’s choice.  The following is an example.
#
# Health and Fitness Program
#
# Enter 1 to calculate BMI only
# Enter 2 to determine whether you have high blood pressure only
# Enter 3 to do both
# Enter your choice: 3
#
# Enter height (in inches): 67
# Enter weight (in pounds): 150
# Your BMI is: 23.490755179327245
#
# Enter your systolic pressure: 132
# Enter your diastolic pressure: 91
# You have high blood pressure.
#
# Save your program in a file named Lab07P2.py.  Submit it to Blackboard for credit.


def main():
    print('LEARN YOUR BODY MASS INDEX (BMI) AND IF YOUR BLOOD PRESSURE (BP) IS IN NORMAL RANGE\n\n')
    print('Enter 1 - To learn about your BMI')
    print('Enter 2 - To learn about your BP')
    print('Enter 3 - To learn about your BMI and BP')
    choice = int(input('\nEnter your selection from the available options above to begin.\t\t\t\t\t\t'))
    user_choice(choice)


def user_choice(a_choice):
    if a_choice == 1:
        bmi()
    elif a_choice == 2:
        bp()
    elif a_choice == 3:
        bmi()
        print()
        bp()
    else:
        print('\nYou did not select a valid option.\n')


def bmi():
    bmi_height = int(input('\nEnter your height in inches:\t\t\t\t\t\t\t\t\t\t\t\t\t\t'))
    bmi_weight = int(input('Enter your weight in pounds:\t\t\t\t\t\t\t\t\t\t\t\t\t\t'))
    bmi_result = (703*bmi_weight)/(bmi_height*bmi_height)
    print('\nYour BMI is ' + format(bmi_result, ',.2f') + "%.")


def bp():
    systolic = int(input('Enter your systolic (top number) from your blood pressure reading:\t\t\t\t\t'))
    diastolic = int(input('Enter your diastolic (bottom number) from your blood pressure reading:\t\t\t\t'))
    if systolic >= 140 or diastolic >= 90:
        print('\nYour BP readings indicate you have high blood pressure.  Consult your doctor.\n')
    else:
        print('\nYour BP readings indicate your blood pressure is within normal range.\n')


main()
