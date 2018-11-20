__author__ = 'Michele Johnson'
# Program Requirements:
# A company is sending its employees to receiving training on some new equipment.  
# The training includes two parts: part A and part B.  
# The cost for attending part A is $100 while the cost for part B is $150.  
# There are three options for each attendee:
# 		Option A: Attend part A only
# 		Option B: Attend part B only
# 		Option C: Attend both part A and part B 
# Attendees who choose option C get a 20% discount.  
# Write a program to calculate how much training fee the company needs to pay in total.  
# The program should ask the user to enter the number of people who choose 
# option A, option B and option C, respectively.  It will calculate and display the total training fee 
# the company needs to pay.

# Get input from user
Num_Emp_Part_A = int(input('Enter the number of employees taking part A of the course:  '))
Num_Emp_Part_B = int(input('Enter the number of employees taking part B of the course:  '))
Num_Emp_Part_AB = int(input('Enter the number of employees taking both parts A and B of the course:  '))

# Calculations
Part_A_Exps = Num_Emp_Part_A * 100
Part_B_Exps = Num_Emp_Part_B * 150
Part_AB_Chrg = 100 + 150
Dsc_Part_AB_Chrg = Part_AB_Chrg * ((100 - 20)/100)
Part_AB_Exps = Num_Emp_Part_AB * Dsc_Part_AB_Chrg
Tot_Exp_Amt = Part_A_Exps + Part_B_Exps + Part_AB_Exps

#Output
print('\nThe cost for', Num_Emp_Part_A, 'employees taking only part A:\t\t$' + (format(Part_A_Exps, ',.2f')))
print('The cost for', Num_Emp_Part_B, 'employees taking only part A:\t\t$' + (format(Part_B_Exps, ',.2f')))
print('The cost for', Num_Emp_Part_AB, 'employees taking both parts A and B:\t$' + (format(Part_AB_Exps, ',.2f')))
print('\nThe total training expense for the company:\t\t\t$' + (format(Tot_Exp_Amt, ',.2f')))
