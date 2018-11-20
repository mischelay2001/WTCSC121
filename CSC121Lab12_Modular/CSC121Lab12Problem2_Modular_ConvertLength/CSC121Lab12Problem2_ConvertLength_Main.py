__author__ = 'Michele Johnson'

# """ Program requirements:
#
#     Create a file for the main module.
#
#     Define a main function in the main module to do the following:
#     (1)	Ask the user to enter lengths in inches, feet and miles
#     (2)	Call the three functions in the length module to convert the lengths
#     (3)	Receive and display the converted lengths """

import convert_length

from Lab14_OOP2_Problem1_MealOrderTemp import valid_entry


def main():
    # Introduce Program
    print("CONVERT LENGTHS\n")
    print("Program will convert lengths submitted by the user"
          "in units of inches, feet, and miles into cm, m, km respectively\n")

    # Call length converting functions

    # Inches to cm
    request_inch = "Enter a length in inches"
    length_inches = valid_entry.float_entry(request_inch)
    convert_inches = convert_length.inch_to_cm(length_inches)
    print(length_inches, "inches equals", convert_inches, "centimeters\n")

    # Feet to miles
    request_feet = "Enter a length in feet"
    length_feet = valid_entry.float_entry(request_feet)
    convert_feet = convert_length.feet_to_m(length_feet)
    print(length_feet, "feet equals", convert_feet, "meters\n")

    # Miles to km
    request_miles = "Enter a length in miles"
    length_miles = valid_entry.float_entry(request_miles)
    convert_miles = convert_length.miles_to_km(length_miles)
    print(length_miles, "miles equals", convert_miles, "kilometers")


main()
