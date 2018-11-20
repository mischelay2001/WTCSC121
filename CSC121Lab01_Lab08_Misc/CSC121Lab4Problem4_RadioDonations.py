__author__ = 'Michele Johnson'
# Program Requirements
# A classical music radio station is currently raising fund.
# Listeners call in to make a donation to support the station.
# Write a program to do the following.
# Ask the user to enter the number of donors today.
# Then use a loop to get the amount donated by each donor. Calculate and display the total donation for the day.

# Introduce program
print('This program will calculate the total donations for the day.\n')

# Declare Variables
count = 0
donor_num = ''
donation = ''
total_donation = 0

raw_input_valid = False
while raw_input_valid is False:
    try:
        donation_num = int(input('How many donations were there today?\t\t'))
        if donation_num > 0:
            raw_input_valid = True
            print("\nGreat!"
                  "\nNow let's capture each donation.\n")
        else:
            print("\nInvalid Entry"
                  "\nThe number of donations must be greater than 0."
                  "\nPlease enter a valid number.\n")
    except ValueError:
        print('\nInvalid Entry'
              '\nThe number of donations must be greater than 0.'
              '\nPlease enter a valid number.\n')

while count < donation_num:
    count = count + 1
    raw_input_valid = False
    while raw_input_valid is False:
        try:
            donation = float(input("Enter the donation amount?\t\t\t\t\t"))
            if donation > 0:
                raw_input_valid = True
                donor_num = count
                total_donation = total_donation + donation
                print('Donor number:', donor_num, 'donated $' + (format(donation, ',.2f') + '.\n'))
            else:
                print('\nInvalid Entry'
                      '\nThe number of donations must be greater than 0.'
                      '\nPlease enter a valid number.\n')
        except ValueError:
                print('\nInvalid Entry'
                      '\nThe number of donations must be greater than 0.'
                      '\nPlease enter a valid number.\n')

    if count < donation_num:
        print("Now let's capture the next donation...\n")
    else:
        print('That was the last donation for today.')

# Output
print('The total donation for today was $' + (format(total_donation, ',.2f') + '.\n'))
