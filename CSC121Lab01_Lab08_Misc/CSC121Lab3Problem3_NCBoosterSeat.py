__author__ = 'Michele Johnson'
# Program Requirements
# North Carolina state law requires all children to ride in a booster seat until
# either the child has reached age 8 or has exceeded 70 pounds.
# Write a program to determine whether a child needs to ride in a booster seat.
# Ask the age and weight of the child, then decide whether booster seat is required.

# Introduce program
print('This program will determine if a child is required to ride in a booster seat per'
      'North Carolina law based on age and/or weight.\n')

# Get age input from user
age = input('Enter the child\'s age: ')
boolean_age_digit = False
boolean_valid_age = False

# Validate age input
while boolean_age_digit is False and boolean_valid_age is False:
    try:
        age = int(age)
        boolean_valid_age = age <= 200
    except ValueError:
        pass
        print('\nInvalid entry.  Please re-enter a valid age for the child.')
        age = input('\nEnter the child\'s age: ')

# Get weight input from user
weight = input('Enter the child\'s weight: ')
boolean_weight_digit = False
boolean_valid_weight = False

# Validate weight input
while boolean_age_digit is False and boolean_valid_weight is False:
    try:
        weight = int(weight)
        boolean_valid_weight = weight <= 1000
    except ValueError:
        pass
        print('\nInvalid entry.  Please re-enter a valid weight for the child.')
        weight = input('\nEnter the child\'s weight: ')

# Compare if input is within requirements
boolean_age_weight = age < 8 or weight < 70

# Output
# Age is less than 8 OR weight is less than 70 lbs
if boolean_age_weight is True:
    print('\nA child', age, 'years of age and', weight,
          'lbs, IS required to ride in a booster seat according to North Carolina state law.')
# Age is greater than or equal to 8 AND weight is greater than or equal to 70 lbs
else:
    print('\nA child', age, 'years of age and', weight,
          'lbs, IS NO longer required to ride in a booster seat according to North Carolina state law.')
