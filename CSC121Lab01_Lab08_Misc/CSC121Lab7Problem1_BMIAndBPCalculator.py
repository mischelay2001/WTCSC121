__author__ = 'Michele Johnson'
# Program Requirements

# A health insurance company wants a program to promote health and fitness.
# This program can do two things: calculate BMI (Body Mass Index) and determine
# whether a person has high blood pressure.
# To calculate BMI, the user must enter his height (in inches) and weight (in pounds).
# Use the following formula to calculate BMI:
#
# 	BMI = (703 * weight) / (height*height)
#
# To determine whether a person has high blood pressure,
# the user must enter his systolic pressure and diastolic pressure.
# If the systolic pressure >= 140 or the diastolic pressure is >= 90, he has high blood pressure.
# Define and use the following two functions in this program:
#
# 	calc_bmi: Get height and weight from the user.  Calculate and display BMI.
# 	hypertension: Get systolic pressure and diastolic pressure from the user.
#
# Determine and display whether the user has high blood pressure.
#
# Also write and use a main function to implement the mainline logic of the program.
# The user calculates BMI first, then determines whether the user has high blood pressure.


def main():
    print('LEARN YOUR BODY MASS INDEX (BMI) AND IF YOUR BLOOD PRESSURE (BP) IS IN NORMAL RANGE\n')
    bmi()
    bp()


def bmi():
    bmi_height = int(input('Enter your height in inches:\t\t\t\t\t'))
    bmi_weight = int(input('Enter your weight in pounds:\t\t\t\t\t'))
    bmi_result = (703*bmi_weight)/(bmi_height*bmi_height)
    print('Your BMI is ' + format(bmi_result, ',.2f') + "%.\n")


def bp():
    systolic = int(input('Enter your systolic (top number) from your blood pressure reading:\t\t\t\t\t'))
    diastolic = int(input('Enter your diastolic (bottom number) from your blood pressure reading:\t\t\t\t'))
    if systolic >= 140 or diastolic >= 90:
        print('Your BP readings indicate you have high blood pressure.  Consult your doctor.\n')
    else:
        print('Your BP readings indicate your blood pressure is within normal range.\n')


main()
