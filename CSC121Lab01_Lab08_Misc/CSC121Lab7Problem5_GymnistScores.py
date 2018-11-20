__author__ = 'Michele Johnson'


# Program Requirements

# Each gymnast in a competition receives scores from 5 judges.
# Write a Python program to do the following.
# (a)	In the main function, ask the user to enter 5 scores.
# Store the scores in a list.
# (b)	Invoke the function score_calculator and pass the whole list to it.
# (c)	In the function score_calculator, calculate and display the average of the 5 scores.


def main():
    i = 0
    score_count = 5
    score_list = []
    print('This program calculates the competition scores from 5 judges\n')
    while i < score_count:
        score = float(input('Enter your score:\t'))
        score_list.append(score)
        i = i + 1
    score_calc(score_list)


def score_calc(a_score_list):
    j = 0
    total_scores = 0
    list_length = len(a_score_list)
    while j < list_length:
        total_scores = total_scores + a_score_list[j]
        j = j + 1
    print('\nThe average score is ' + (format(total_scores, ',.2f')) + '.')


main()
