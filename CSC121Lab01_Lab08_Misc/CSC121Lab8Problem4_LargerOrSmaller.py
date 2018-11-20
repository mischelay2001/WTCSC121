__author__ = 'Michele Johnson'

# Program Requirements
# Write a program to do the following.  Ask the user to enter two numbers.  Compare them and display the larger one
# and the smaller one.  Define and use the following functions:
#
# get_numbers: Ask user to enter two numbers.  Use a return statement to return them.
#
# large_small: Compare two numbers.  Use a return statement to return the larger number and the smaller number
#
# Also write a main function to implement the mainline logic.  Call the get_numbers function to get two numbers.
# Then call the large_small function and pass the two numbers as arguments.  Display the larger and the smaller
# numbers in main.

# Introduce Program
print("COMPARE NUMBERS\n")
print("This program will: "
      "\n\tAsk for two numbers, "
      "\n\tCompare them, and "
      "\n\tReport which is the largest and the smallest number.\n")


def main():
    # Main function for COMPARE NUMBERS program
    # Function will receive two numbers, and display if which is the larger and the smaller number, or
    # Will display if the numbers are equal
    num1, num2 = get_numbers()
    print()
    if num1 == num2:
        print("The numbers are equal.")
    else:
        larger, smaller = compare_numbers(num1, num2)
        print(larger, "is the larger number.", )
        print(smaller, "is the smaller number.")


def get_numbers():
    # Function to obtain two numbers
    # Will return numbers obtained
    def valid_entry_num1():
        # Function to obtain valid entry per program requirements
        # Will ask user for input per program requirements
        # Will return an error message if entry is invalid

        # Initiate test variable to false
        is_entry_valid = False
        # Initiate entry variable to match correct variable type and value: number; 0.0
        entry = 0.0
        while is_entry_valid is False:
            try:
                entry = float(input("Enter the first number:\t\t"))
                if entry >= 0:
                    is_entry_valid = True
                else:
                    print("Invalid Entry\n")
            except ValueError:
                pass
                print("\nInvalid Entry\n")
        return entry

    def valid_entry_num2():
        # Function to obtain valid entry per program requirements
        # Will ask user for input per program requirements
        # Will return an error message if entry is invalid

        # Initiate test variable to false
        is_entry_valid = False
        # Initiate entry variable to match correct variable type and value: number; 0.0
        entry = 0.0
        while is_entry_valid is False:
            try:
                entry = float(input("Enter the second number:\t"))
                if entry >= 0:
                    is_entry_valid = True
                else:
                    print("Invalid Entry\n")
            except ValueError:
                pass
                print("\nInvalid Entry\n")
        return entry

    entry1 = valid_entry_num1()
    entry2 = valid_entry_num2()
    return entry1, entry2


def compare_numbers(a_num1, a_num2):
    # Function to compare two numbers
    # Will return the largest first and smallest second
    if a_num1 > a_num2:
        a_large = a_num1
        a_small = a_num2
    else:
        a_large = a_num2
        a_small = a_num1
    return a_large, a_small


main()
