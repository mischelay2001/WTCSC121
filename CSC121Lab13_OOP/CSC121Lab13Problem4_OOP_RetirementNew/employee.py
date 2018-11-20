__author__ = 'Michele Johnson'

""" Write a new version of the Retirement project you wrote in Problem 2.  
Create a new Python project RetirementNew and copy the files from the old project.  
Make the following changes to class Employee:

(a)	Change all instance variables to private
(b)	Write setter methods for salary and years of service.
(c)	Define a __str__ method to display the employee’s name, salary and years of service.

Employee
    -emp_name: String
    -salary: Float
    -years_service: Float
    -final: Float
    +create(emp_name: String, salary: Float, years_service: Float)
    +pension(): Float
    +set_salary(): Float
    +set_years(): Integer  """


class Employee:

    """ creates three publicly accessible instance variables to store employee’s name, salary, and years of service."""

    def __init__(self, employee_name, employee_salary, employee_years_service):

        """ constructor of class Car """

        self.__name = employee_name
        self.__salary = employee_salary
        self.__years = employee_years_service

    def pension(self):

        """ calculate the monthly pension payout the employee will receive in retirement """

        payout = self.__salary * self.__years * 0.0015

        return payout

    def set_salary(self, employee_salary):

        """ receives employee salary and stores value in salary """

        self.__salary = employee_salary

    def set_years(self, employee_years_service):

        """ receives employee years of service and stores value in years """

        self.__years = employee_years_service

    def __str__(self):

        """ convert class to string """

        return '\nEmployee Name:\t\t\t\t\t' + self.__name + '\n\tEmployee Salary:\t\t\t$' + str(
            (format(self.__salary, ',.2f'))) + '\n\tYears of Service:\t\t\t' + str(
            self.__years)
