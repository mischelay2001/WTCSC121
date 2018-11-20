debates = 5
i = 0
dem_won = 0
rep_won = 0

while i < debates:
    print("Debate ", i+1)
    percent_won_dem = int(input("Enter the percentage the Dem won."))
    percent_won_rep = int(input("Enter the percentage the Rep won."))
    print()
    percent_difference = abs(percent_won_dem - percent_won_rep)
    if percent_difference <= 3:
        print("It's a tie\n")
    elif percent_won_dem > percent_won_rep:
        print("Dem won\n")
        dem_won = dem_won + 1
    else:
        print("Rep won\n")
        rep_won = rep_won + 1
    i = i + 1
print("Democrat won ", dem_won)
print("Republican won ", rep_won)
print()
if dem_won == rep_won:
    print("Candidates won the same number of debates.")
elif dem_won > rep_won:
    print("The democrat won the most debates")
else:
    print("The republican won the most debates.")
