# (Find future dates) Write a program that prompts the user to enter an integer for
# today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
# prompt the user to enter the number of days after today for a future day and display
# the future day of the week.


today = eval(input("Enter Today's Day: "))
noOfDays = eval(input("Enter no. of days Elapsed"))
finalDay = (today+noOfDays)%7
x=""

if finalDay == 0:
    x="Sunday"
elif finalDay == 1:
    x="Monday"
elif finalDay == 2:
    x="Tuesday"
elif finalDay == 3:
    x="Wednesday"
elif finalDay == 4:
    x="Thursday"
elif finalDay == 5:
    x="Friday"
elif finalDay == 6:
    x="Saturday"

print("The future day is", x)