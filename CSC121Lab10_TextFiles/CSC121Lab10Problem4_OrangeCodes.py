__author__ = 'Michele Johnson'


# Program Requirements
# All oranges sold in a grocery store have a 4-digit product code.  If the rightmost digit is '4',
# the orange is from California.  If the rightmost digit is '7', the orange is from Florida.
# For example, an orange with product code '8124' is from California.
# An orange with product code '6547' is from Florida.  Write a program to do the following:
#
# (a)	Ask the user to enter the 4-digit code of an orange.
# (b)	Strip all the leading and trailing whitespace characters from the code.
# (c)	Test whether the code consists of only numeric digits.  If it is not, display an error message.
# (d)	Test whether the code has exactly 4 characters.
# If it has more or fewer than 4 characters, display an error message.
# (e)	Test the rightmost digit.  If it is '4', display 'This orange is from California'.
# If it is '7', display 'This orange is from Florida'.
# If it is something else, display 'The last digit must be 4 or 7'.


# Main function
def main():
    # Introduce Program
    print("ORANGE ORIGINATION CODE\n\n"
          "Program will determine the state of origination of orange produce per the 4-digit product code.\n")

    # Declare variables
    code = valid_entry1()
    fourth_char = code[3]
    # Test fourth digit and display the appropriate message.
    if fourth_char is '4':
        print("California is the state of origin for this orange.")
    elif fourth_char is '7':
        print("Florida is the state of origin for this orange.")
    else:
        print("The last digit of the product code must be a 4 or 7 to determine state of origin.")


def valid_entry1():
    # Check input is valid: product code
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value: string as 4-digits
    entry = 0
    while is_entry_valid is False:
        try:
            entry = str(input("Enter the 4-digit product code for the oranges as an integer:\t"))
            length = len(entry)
            is_digit = entry.isdigit()
            if length is 4 and is_digit is True:
                is_entry_valid = True
            else:
                print("Invalid Entry\n")
        except ValueError:
            pass
            print("\nInvalid Entry\n")
    return entry


main()
