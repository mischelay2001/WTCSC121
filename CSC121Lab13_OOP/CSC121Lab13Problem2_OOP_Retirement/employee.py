__author__ = 'Michele Johnson'

""" Create a Python project Retirement.  Add a Python file employee.py to this project.  
Define a class Employee in this file.  In this class, create three publicly accessible instance variables to store 
employee’s name, salary, and years of service.  Define the following methods:

(a)	A __init__ method that accepts the employee’s name, salary and years of service as arguments.  
Write statements in __init__ to store them in instance variables.  

(b)	A pension method to calculate the monthly pension payout the employee will receive in retirement: 
monthly pension payout = salary * years of service * 0.0015.  No arguments need to be passed to this method when this 
method is called.  It uses data stored in the instance variables to calculate monthly pension payout.  
This method returns the monthly pension payout.

Employee
    +emp_nsme: String
    +salary: Float
    +years_service: Float
    +final: Float
    +create(emp_name: String, salary: Float, years_service: Float)
    +pension(): Float"""


class Employee:

    """ creates three publicly accessible instance variables to store employee’s name, salary, and years of service."""

    def __init__(self, employee_name, employee_salary, employee_years_service):

        """ constructor of class Car """

        self.name = employee_name
        self.salary = employee_salary
        self.years = employee_years_service

    def pension(self):

        """ calculate the monthly pension payout the employee will receive in retirement """

        payout = self.salary * self.years * 0.0015

        return payout

    def __str__(self):

        """ convert class to string """

        return 'Employee Name:\t\t\t\t\t' + self.name + '\n\tEmployee Salary:\t\t\t$' + str(
            (format(self.salary, ',.2f'))) + '\n\tYears of Service:\t\t\t' + str(
            self.years)
