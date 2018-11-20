__author__ = 'Michele Johnson'

# Program Requirements

# Write a program to calculate target heart rate during fitness training.
# This program has two functions: main and heart_rate_calculator.  Please do the following:

# (a)	In the main function, ask the user to enter age and resting heart rate.
# (b)	In the main function, call the heart_rate_calculator function.
# Pass the age and resting heart rate as arguments.
# (c)	In the heart_rate_calculator function,
# write code to calculate target heart rate during fitness training with the following formula:

# Target hart rate = (220 - age - resting heart rate) * 0.4 + resting heart rate

# Display target heart rate.


def main():
    print('This program will calculate target heart rate during fitness training.\n')
    age = int(input('Enter your age.\t\t\t\t\t\t\t'))
    resting = float(input('Enter your resting heart rate reading.\t'))
    heart_rate(age, resting)


def heart_rate(a_age, a_resting):
    rate = (220 - a_age - a_resting) * 0.4 + a_resting
    print('Your heart rate is ' + (format(rate, ',.2f')) + '.')


main()
