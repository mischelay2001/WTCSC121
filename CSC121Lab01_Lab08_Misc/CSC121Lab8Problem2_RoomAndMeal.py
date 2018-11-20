__author__ = 'Michele Johnson'
# Program Requirements
# All freshmen of ABC College must live on campus.  Single room is $3000 per semester, while double room is $2000
# per semester.  There are also two meal plans to choose.  The 21-meal plan serves 21 meals each week with the price of
# $3500 per semester.  The 15 mean plan serves 15 meals each week with the price of $2800 per semester.
#
# Write a program for a freshman to choose room type and meal plan.  Define and use the following two functions:
#
# choose_room: Display room types and get user choice. Display user choice.
# choose_meal: Display meal plans and get user choice. Display user choice.
#
# Each of these functions returns the price of the chosen item.  You are allowed to write only one return statement in
# each function.
#
# Write a main function to implement the mainline logic of the program.  Calculate and display the total price in the
# main function.

# Introduce Program
print("SEMESTER COST FOR HOUSING AND MEALS\n")
print("This program will calculate the total cost of housing and meals per semester.")


def main():
    # Main function for the SEMESTER COST FOR HOUSING AND MEALS program
    # Function will ask for users room and meal choice
    # Will display choices to confirm and total cost for housing and meals
    room = choose_room()
    print()
    meals = choose_meal()
    total_cost = room + meals
    print("\nSEMESTER COST FOR HOUSING AND MEALS\n")
    print("Housing:\t$" + format(room, ',.2f'))
    print("Meals:\t\t$" + format(meals, ',.2f'))
    print("\nThe total cost for housing and meals for the semester is $" + format(total_cost, ',.2f') + ".")


def choose_room():
    # Function for room choice selection
    # Obtain valid entry choice from user: S or D
    # Display user's choice
    # Assigns and returns cost of room
    print("All freshmen of ABC College must live on campus:"
          "\n\tSingle room is $3000 per semester."
          "\n\tDouble room is $2000 # per semester.")
    print("\nPlease make your room selection:")

    def valid_entry():
        # Function to obtain valid entry per program requirements
        # Will ask user for input per program requirements
        # Will return an error message if entry is invalid
        # Initiate test variable to false
        is_entry_valid = False
        # Initiate entry variable to match correct variable type and value: string/Null
        entry = ""
        while is_entry_valid is False:
            try:
                entry = str(input("\tEnter 'S' for single room or 'D' for double room.\t"))
                entry = entry.upper()
                print()
                if entry == 'S' or entry == 'D':
                    is_entry_valid = True
                    if entry == 'S':
                        print("A single room for housing was selected.")
                    elif entry == 'D':
                        print("A double room for housing was selected.")
                else:
                    print("Invalid Entry\n")
            except ValueError:
                pass
        return entry

    room_entry = valid_entry()
    if room_entry == 'S':
        a_room_cost = 3000
    else:
        a_room_cost = 2000
    return a_room_cost


def choose_meal():
    # Function for meal choice selection
    # Obtain valid entry choice from user: 1 or 2
    # Display user's choice
    # Assigns and returns cost of meals
    print("There are two meal plans to choose from:"
          "\n\tThe 21-meal plan serves 21 meals each week with the price of $3500 per semester.  "
          "\n\tThe 15 mean plan serves 15 meals each week with the price of $2800 per semester.")
    print("\nPlease make your meal selection:")

    def valid_entry():
        # Function to obtain valid entry per program requirements
        # Will ask user for input per program requirements
        # Will return an error message if entry is invalid
        # Initiate test variable to false
        is_entry_valid = False
        # Initiate entry variable to match correct variable type and value: integer; 0
        entry = 0
        while is_entry_valid is False:
            try:
                entry = int(input("\tEnter 1 for the 21-meal plan.  Enter 2 for the 15-meal plan.\t"))
                print()
                if entry == 1 or entry == 2:
                    is_entry_valid = True
                    if entry == 1:
                        print("The 21-meal plan was selected.")
                    elif entry == 2:
                        print("The 15-meal plan was selected.")
                else:
                    print("Invalid Entry\n")
            except ValueError:
                pass
                print("\nInvalid Entry\n")
        return entry

    meal_entry = valid_entry()
    if meal_entry == 1:
        a_meal_cost = 3500
    else:
        a_meal_cost = 2800
    return a_meal_cost


main()
