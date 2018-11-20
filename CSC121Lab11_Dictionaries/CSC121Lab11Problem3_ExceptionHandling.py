__author__ = 'Michele Johnson'

# This program is about exception handling.  Write a program to calculate the area of a circle.
# Ask the user to enter the radius of the circle.
# If the radius is invalid (i.e. something that cannot be converted to a floating point value),
# display “Invalid input” and terminate the program.  Otherwise, calculate and display the area.


import math


def main():
    # Program statements when entry is a float
    try:
        # Introduce Program
        print("This program is about exception handling.\n")
        print("Program will calculate the area of a circle given the radius from the user."
              "\nIf the entry for the user is invalid, an error message will be displayed and program will terminate.\n")

        # Get radius from user
        print("Calculate Area of a Circle")
        radius = float(input("Enter the radius:\t "))

        # Calculate circle area and display
        print("\nRadius entered:\t\t", radius)
        area = round(math.pi * pow(radius, 2), 4)
        print("Circle area:\t\t", area)

    # Invalid entry error handling and message
    except ValueError:
        pass
        print("\nInvalid Entry\nEnd Program")


main()
