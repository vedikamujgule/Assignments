# (Sum a series) Write a program to sum the following series:

sum = 0
for i in range(1, 98):
    sum += i / (i + 2)

print("The sum of the series is: ", sum)