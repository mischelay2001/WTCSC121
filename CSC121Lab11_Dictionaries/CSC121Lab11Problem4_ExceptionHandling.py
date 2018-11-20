__author__ = 'Michele Johnson'

# This program is about exception handling.  Write a program to calculate the area of a circle.
# Ask the user to enter the radius of the circle.
# If the radius is invalid (i.e. something that cannot be converted to a floating point value),
# display “Invalid input” and continue to request the user to enter a valid entry.
# Otherwise, calculate and display the area.


import math


def main():
    # Introduce Program
    print("This program is about exception handling.\n")
    print("Program will calculate the area of a circle given the radius from the user."
          "\nIf the entry for the user is invalid, an error message will be displayed and re-ask for valid entry.\n")

    # Calculate circle area and display
    print("Calculate Area of a Circle")
    radius = valid_entry1()
    print("\nRadius entered:\t\t", radius)
    area = round(math.pi * pow(radius, 2), 4)
    print("Circle Area:\t\t", area)


def valid_entry1():
    # Check input is valid: radius
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid: float as string

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value: float
    entry = ""
    while is_entry_valid is False:
        try:
            entry = float(input("Enter the radius:\t "))
            is_entry_valid = True

        # Invalid entry error handling and message
        except ValueError:
            pass
            print("\nInvalid Entry\n")
    return entry


main()
