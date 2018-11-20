def integer_entry(a_request_text):
    # Check input is valid
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value
    entry = ""
    while is_entry_valid is False:
        try:
            entry = int(input(a_request_text + ":\t "))
            is_entry_valid = True

        # Invalid entry error handling and message
        except ValueError:
            pass
            print("\nInvalid Entry\n")
    return entry


def float_entry(a_request_text):
    # Check input is valid
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value: float
    entry = ""
    while is_entry_valid is False:
        try:
            entry = float(input(a_request_text + ":\t "))
            is_entry_valid = True

        # Invalid entry error handling and message
        except ValueError:
            pass
            print("\nInvalid Entry\n")
    return entry

def clean_string_digits(a_request_text, digit_length):
    # Check input is valid
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value: string
    entry = ""
    while is_entry_valid is False:
        entry = str(input(a_request_text + ":\t "))
        # Clean unwanted characters
        entry = entry.strip()
        clean_chr = ["(", ")", "-", ".", " "]
        for i in clean_chr:
            entry = entry.replace(i, "")
        # Check for validity digits
        is_digit = entry.isdigit()
        entry_length = len(entry)
        if (is_digit is False) or (entry_length != digit_length):
            # Output to display
            print("The entry is not a valid.")
        else:
            is_entry_valid = True
    return entry
