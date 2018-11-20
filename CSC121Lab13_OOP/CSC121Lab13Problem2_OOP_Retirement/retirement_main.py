__author__ = 'Michele Johnson'

""" Program requirements:

Add a file retirement_main.py to this project.  This is the main module.  
Write code to ask the user to enter name, salary and years of service of two employees.  
Create two instances of Employee.  Call the pension method of these objects to calculate pensions.  
Display the pensions.  """

from employee import Employee

from Lab14_OOP2_Problem1_MealOrderTemp import valid_entry


def main():

    #Introduce Program
    print("RETIREMENT\n")
    print("Program will calculate an employee's monthly pension payout.\n")

    # Initialize variables
    employee_count = 2

    # Loop until all employees processed
    for i in range(employee_count):
        # Get user entries
        entry_name = str(input("Employee Name:\t\t\t\t\t\t"))
        entry_salary = valid_entry.entry_salary()
        entry_years = valid_entry.entry_years()

        # Initialize Employee class
        a_employee = Employee(entry_name, entry_salary, entry_years)
        a_payout = a_employee.pension()
        print("\n", a_employee)
        print('\tMonthly Pension Payout:\t\t$' + str((format(a_payout, ',.2f'))) + "\n")

main()
