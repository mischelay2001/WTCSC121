__author__ = 'Michele Johnson'
# Program Requirements
# There are two exams in a programming course.  Write a program to calculate a student’s total score.
# To encourage students to do better in the final exam, if a student has improved by more than 20 points
# from midterm to final, the student will receive 5 bonus points in the total.
# Write a Python program to do the following.  Calculate and display total score before bonus.
# If a student receives extra points, display a text message about improvement bonus and new total score.

# Introduce program
print('Students that increase their midterm score by at least 20 points on their final will earn a 5 point bonus.\n')

# Get input from user
midterm = int(input('Enter student\'s midterm score:  '))
final = int(input('Enter student\'s final exam score:  '))

# Calculations
total_score = midterm + final
difference = final - midterm
bonus_total_score = midterm + final + 5

# Output the total score
print('\nYour total score for the course is ', total_score, '.', sep='')
# Does not get bonus if difference is less than 20, complete the following:
if difference < 20:
    print('\nYour score did not improve by 20 points. \nYou are not eligible for the bonus.')
# Gets bonus if difference is greater than or equal to 20, complete the following:
else:
    print('\nGreat job!  You improved your score by ', difference, ' points. \nYou earned a 5 point bonus. '
          '\n\nYour final score for the course including the bonus is ',  bonus_total_score,  '.',  sep='')
