# (Find the number of years and days) Write a program that prompts the user to
# enter the minutes (e.g., 1 billion), and displays the number of years and days for
# the minutes.

min = int(input("Enter the number of minutes: "))
years = int(min / (365 * 24 * 60))
peningMin = min % (365 * 24 * 60)
days = int(peningMin / (24 * 60))
print(min, "minutes is approximately", years, "years and", days, "days")

