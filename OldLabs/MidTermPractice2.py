high_temp = []
sum_temp = 0.0
i = 0
j = 0
days_high = 0
while i < 5:
    temp = int(input("Enter the high temperature for today"))
    high_temp.append(temp)
    sum_temp = sum(high_temp)
    i = i + 1
print(high_temp)
avg_temp = sum_temp / len(high_temp)
while j < len(high_temp):
    if avg_temp > high_temp[j]:
        days_high = days_high + 1
    j = j + 1
print("Temperatures entered", high_temp)
print("Lowest temperature: ", min(high_temp))
print("Highest temperature: ", max(high_temp))
print("Average temperature: ", avg_temp)
print("Number of days hotter than average: ", days_high)
