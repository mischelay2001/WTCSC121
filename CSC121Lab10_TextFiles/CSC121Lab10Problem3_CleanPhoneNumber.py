__author__ = 'Michele Johnson'


# Program Requirements
# When people enter phone numbers, they typically enter it in a few different formats:
#
# 	(919)866-5555
# 	919-866-5555
# 	9198665555
#
# Write a program to delete all occurrences of these characters: '(', ')' and '-'.
# Also, strip all the leading and trailing whitespace characters.


# Main function
def main():
    # Introduce Program
    print("CLEAN PHONE NUMBER\n\n"
          "Program will strip phone number entry of the following characters:  '(', ')', '-', '.', and spaces.\n")

    # Declare variables
    entry = str(input("Please enter a phone number:\t"))
    # Clean unwanted characters
    entry = entry.strip()
    clean_chr = ["(", ")", "-", ".", " "]
    for i in clean_chr:
        entry = entry.replace(i, "")
    # Check for validity of phone number
    is_digit = entry.isdigit()
    entry_length = len(entry)
    if is_digit is False and (entry_length != 10 or entry_length != 9):
    # Output to display
        print("The entry is not a valid phone number: ", entry)
    else:
        print("The phone number has been cleaned: ", entry)


main()
