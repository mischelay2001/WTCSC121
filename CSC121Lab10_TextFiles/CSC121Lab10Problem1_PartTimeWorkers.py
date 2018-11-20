__author__ = 'Michele Johnson'

# Program Requirements
# A toy store has 4 part-time workers who are paid by hours.  Each worker has a worker ID number.
# Write a program that asks for the worker ID number, the hourly rate and the number of work hours per week of
# each worker.  The program should store the data in a text file named “workers.txt”.
# Overwrite old data in “workers.txt” if the file already exists.


# Main function
def main():
    # Introduce Program
    print("PART-TIME WORKER INFORMATION\n\n"
          "Program will collect the worker ID, hourly rate, and number hours worked for part-time employees.\n"
          "The worker information entered will be displayed and stored in text file, CSC11_workers.txt.\n")

    # Declare variables
    num_workers = 4
    output_file = open('CSC121_workers.txt', 'w')
    # Loop through number of workers for each line of data
    # Convert data into string and clean unwanted characters
    for i in range(num_workers):
        worker_info = str(get_entries()) + "\n"
        clean_chr = ["(", ")", " "]
        for j in clean_chr:
            worker_info = worker_info.replace(j, "")
        # Output to display and text file
        print(worker_info)
        output_file.write(worker_info)
    output_file.close()


def get_entries():
    # Get user entries: worker ID, hourly rate, hours worked
    # Function to obtain valid user entries per program requirements

    def valid_entry1():
        # Check input is valid: worker ID
        # Function to obtain valid entry per program requirements
        # Will ask user for input per program requirements
        # Will return an error message if entry is invalid

        # Initiate test variable to false
        is_entry_valid = False
        # Initiate entry variable to match correct variable type and value: integer; 0
        entry = 0
        while is_entry_valid is False:
            try:
                entry = int(input("Enter the worker ID as an integer:\t"))
                if entry >= 0:
                    is_entry_valid = True
                else:
                    print("Invalid Entry\n")
            except ValueError:
                pass
                print("\nInvalid Entry\n")
        return entry

    a_worker_id = valid_entry1()

    def valid_entry2():
        # Check input is valid: hourly rate
        # Function to obtain valid entry per program requirements
        # Will ask user for input per program requirements
        # Will return an error message if entry is invalid

        # Initiate test variable to false
        is_entry_valid = False
        # Initiate entry variable to match correct variable type and value: number; 0.0
        entry = 0.0
        while is_entry_valid is False:
            try:
                entry = float(input("Enter the hourly rate:\t\t\t\t"))
                if entry >= 0:
                    is_entry_valid = True
                else:
                    print("Invalid Entry\n")
            except ValueError:
                pass
                print("\nInvalid Entry\n")
        return entry

    a_hourly = valid_entry2()

    def valid_entry3():
        # Check input is valid: hours worked
        # Function to obtain valid entry per program requirements
        # Will ask user for input per program requirements
        # Will return an error message if entry is invalid

        # Initiate test variable to false
        is_entry_valid = False
        # Initiate entry variable to match correct variable type and value: number; 0.0
        entry = 0.0
        while is_entry_valid is False:
            try:
                entry = float(input("Enter the hours worked:\t\t\t\t"))
                if entry >= 0:
                    is_entry_valid = True
                else:
                    print("Invalid Entry\n")
            except ValueError:
                pass
                print("\nInvalid Entry\n")
        return entry

    a_hours = valid_entry3()

    return a_worker_id, a_hourly, a_hours


main()
