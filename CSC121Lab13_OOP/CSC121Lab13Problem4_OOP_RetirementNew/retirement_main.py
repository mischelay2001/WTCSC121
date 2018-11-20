__author__ = 'Michele Johnson'

""" Program requirements:

Write a new version of the Retirement project you wrote in Problem 2.  
Create a new Python project RetirementNew and copy the files from the old project.  

Do the following in the main module:

(a)	Get name, salary and years of service from the user and use the input data to create one instance of Employee
(b)	Display the Employee instance with a print statement
(c)	Write a loop to allow the user to change salary and years of service.  
Inside the loop, ask the user to enter 1 to change salary, 2 to change years of service or 3 to exit the loop.  
Make changes to the Employee object.
(d)	Display the Employee object with a print statement again
(e)	Call the pension method of the Employee instance to calculate pension.  Display pension. """

from employee import Employee

from CSC121FinalProject_WakeMartUpgrade import valid_entry


def main():
    # Introduce Program
    print("RETIREMENT II\n")
    print("Program will calculate an employee's monthly pension payout.\n")

    # Initialize variables
    user_choice = 0

    # Get user entries
    entry_name = str(input("Employee Name:\t\t\t\t\t\t"))
    entry_salary = valid_entry.entry_salary()
    entry_years = valid_entry.entry_years()

    # Initialize Employee class
    a_employee = Employee(entry_name, entry_salary, entry_years)
    a_payout = a_employee.pension()
    print(a_employee)
    print('\tMonthly Pension Payout:\t\t$' + str((format(a_payout, ',.2f'))) + "\n")

    # Loop until user selects to exit
    while user_choice != 3:

        # Get valid menu choice
        user_choice = valid_entry.entry_choice()

        # Handle menu selection
        if user_choice == 3:
            print(a_employee)

        else:
            # Get user entries
            print()
            if user_choice == 1:
                entry_salary = valid_entry.entry_salary()
                print("Updated Salary\t\t\t\t\t" + (format(entry_salary, ',.2f')))
            elif user_choice == 2:
                entry_years = valid_entry.entry_years()
                print("Updated Years of Service\t\t\t" + (format(entry_years, ',.2f')))

            # Re-Initialize Employee class
            a_employee = Employee(entry_name, entry_salary, entry_years)
            a_payout = a_employee.pension()
            print(a_employee)
            print('\tMonthly Pension Payout:\t\t$' + str((format(a_payout, ',.2f'))) + "\n")


main()
