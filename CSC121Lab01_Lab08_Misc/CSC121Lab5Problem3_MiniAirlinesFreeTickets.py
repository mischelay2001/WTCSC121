__author__ = 'Michele Johnson'
# Program Requirements

# Mini Airlines awards free tickets to passengers when they have accumulated enough mileages.
# Write a program for passengers to record flight mileages.
# The program will ask the user to enter the mileage of each flight.
# Every time the user has entered a new flight, display the total mileage
# the passenger has accumulated and the number of flights he has taken so far.
# The passenger enters one flight after another until
# he tells the computer he no longer wants to enter another flight.
# Before the program ends, display the mileage of each flight the user has entered in a separate line.

# Introduce program

print('This program will calculate accumulated mileage.\n')

# Declare Variables

total_mileage = []
num_flights = 0
end_program = 1
flight_count = 0
sum_mileage = 0

# Get input from user

while end_program is 1:
    mileage = int(input('Please enter your mileage.\t\t\t\t\t\t\t\t\t\t\t\t\t\t'))
    total_mileage.append(mileage)
    sum_mileage = sum_mileage + total_mileage[flight_count]
    flight_count = flight_count + 1

    # Output for each flight

    print('')
    print(mileage, ' miles were logged for Flight ', flight_count, '.', sep='')
    print('A total of', sum_mileage, 'miles have been logged for a total of', flight_count, 'flight(s).')
    end_program = int(input("\nEnter '1' if you have more mileage to record, or '2' to end the program.\t\t\n"))

# Output for summary

print('Here is a summary of all the flights logged:\n')
while num_flights < flight_count:
     print(total_mileage[num_flights], ' miles were logged for Flight ', (num_flights + 1), '.', sep='')
     num_flights = num_flights + 1
print('\nTotal Accumulated Mileage:\t\t', sum_mileage)
print('Total Flights:\t\t\t\t\t', flight_count)
