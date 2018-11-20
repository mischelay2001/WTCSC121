__author__ = 'Michele Johnson'


# This program is about dictionaries.  We want to store number of students enrolled in each course in a dictionary.
# Write a Python program to do the following:
#
# (a) Create a dictionary to store the following data:
#
# Course	Number of students
# CSC121	55
# CSC131	42
# CSC141	20
# CSC151	25

def main():
    #Introduce Program:
    print("This program demonstrates the use of dictionaries."
          "\nFor this program, course codes and the number of students has been provided to create a dictionary."
          "\nSeveral manipulations of the dictionary will be executed and the results displayed.\n\n")

    num_students = {'CSC121': 55, 'CSC131': 42, 'CSC141': 20, 'CSC151': 25}
    print("The dictionary, num_students, has been created and contains:")
    print(num_students)

    # (b) Write a statement to change the number of students enrolled in CSC121 to 65.
    key = 'CSC121'
    num_students[key] = 65
    print("\nThe number of students enrolled in", key, "has been changed to", num_students[key])

    # (c) Write a statement to add a new course CSC161, which has 17 students enrolled.
    key = 'CSC161'
    num_students[key] = 17
    print()
    print(key, "has been added listing", num_students[key], "students enrolled.")
    print("num_students dictionary now contains:")
    print(num_students)

    # (d) Ask the user to enter a course code.  Test whether this course is in the dictionary.
    print("\nSearch by course number")
    course = valid_entry1()

    # If it is not in the dictionary, display a message saying it is not found.  If it is in the dictionary,
    if course in num_students:
        print()
        print(course, "is a valid course number")

        # display the number of the students enrolled in that course.  Then remove that item from the dictionary.
        print("There are", num_students[course], "students enrolled.")
        del (num_students[course])
        print()
        print(course, "has been removed."
                             "\nnum_students dictionary now contains:")
        print(num_students)

        # (e) Find out the number of items in the dictionary.  Display the number.
        num_courses = len(num_students)
        print("\nThere are", num_courses, "courses:\n")

        # (f) Display every course in the dictionary in this format: (“course code”, enrollment).
        print("Dictionary items in (key, value) format:")
        num_students_dic_items = num_students.items()
        for item in num_students_dic_items:
            print(item)

        print("\nCourse Code\t\t\tNumber of Students Enrolled")
        for key in num_students:
            enrolled = num_students[key]
            print(key, "\t\t\t\t\t\t\t", enrolled)
    else:
        print(key + " is not a valid course number.")


def valid_entry1():
    # Check input is valid: suffix of course
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value: string as 3-digits
    entry = ""
    while is_entry_valid is False:
        try:
            entry = str(input("Enter the 3-digit suffix for the CSC course:\t"))
            entry = entry.strip()
            length = len(entry)
            is_digit = entry.isdigit()
            if length is 3 and is_digit is True:
                is_entry_valid = True
            else:
                print("Invalid Entry\n")

        # Invalid entry error handling and message
        except ValueError:
            pass
            print("\nInvalid Entry")
        entry = "CSC" + str(entry)
    return entry


main()
