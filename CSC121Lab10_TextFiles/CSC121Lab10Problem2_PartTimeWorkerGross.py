__author__ = 'Michele Johnson'

# Program Requirements
# Write a program to read data stored in “workers.txt”, which was created in Problem 1 and has data of 4 workers in it.
# Calculate the gross pay for each worker (gross pay = hourly rate * number of work hours).
# Display worker ID and the gross pay of each worker on computer screen.


# Main function
def main():
    # Introduce Program
    print("PART-TIME WORKER GROSS PAY\n\n"
          "Program will calculate the gross pay for part-time employees \n"
          "per worker information stored in text file, "
          "CSC11_workers.txt.\n")

    # Declare variables, open data text file, initialize reading of first data line
    empty_line = ""
    input_file = open('CSC121_workers.txt', 'r')
    data = input_file.readline()

    # Loop through each line of data
    while data != empty_line:
        # Split data line into appropriate variables
        data = data.strip()
        worker_info = data.split(",")
        worker_id = worker_info[0]
        hourly = float(worker_info[1])
        hours = float(worker_info[2])
        # Calculate Gross
        gross = hourly * hours
        # Output to display
        print("Worker ID:", worker_id, "\tGross: $" + (format(gross, '.2f')))
        data = input_file.readline()
    input_file.close()


main()
