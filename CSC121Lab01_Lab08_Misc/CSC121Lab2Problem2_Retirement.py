__author__ = 'Michele Johnson'
#Program requirements:
# The retirement account of each employee in a company receives money from two sources each month.
# First, each employee contributes 6% of his salary to his own retirement account.
# Second, the company also makes a contribution equal to 3 % of the employee’s salary to the account.
# For example, suppose the monthly salary of an employee is $2000.
# The employee’s own contribution will be $120, while the company’s contribution will be $60.
# They need a program to manage the retirement accounts.  The user will enter the monthly salary of an employee.
# The program will calculate and display the following items: amount of money contributed by the employee each month,
# amount of money contributed by the company each month, total contribution each month
# (i.e. the sum of employee’s and company’s contributions).
# Use 6% and 3% directly in the algorithm to calculate employee’s and company’s contributions.
# There is no need to ask the user to enter these rates.

#Calculations
Emp_Mon_Salary = float(input('Enter the employee\'s monthly salary: '))
Employee_Cont = Emp_Mon_Salary * 0.06
Employer_Cont = Emp_Mon_Salary * 0.03
Com_Cont = Employee_Cont + Employer_Cont

#Output
print('\nBased on the employee\'s monthly salary of $' + (format(Emp_Mon_Salary, '.2f')) + ':\n')
print('The employee\'s monthly contribution at 6% is $' + (format(Employee_Cont, '.2f')) + '.')
print('The employer\'s monthly contribution at 3% is $' + (format(Employer_Cont, '.2f')) + '.')
print('\nThe combined monthly contribution from the employee and employer is $'+ (format(Com_Cont,'.2f')) + '.')
