# (Financial application: compound value) Suppose you save $100 each month into
# a savings account with an annual interest rate of 5%. Therefore, the monthly interest
# rate is 0.05/12 = 0.00417. After the first month, the value in the account
# becomes
# 100 * (1 + 0.00417) = 100.417
# After the second month, the value in the account becomes
# (100 + 100.417) * (1 + 0.00417) = 201.252
# After the third month, the value in the account becomes
# (100 + 201.252) * (1 + 0.00417) = 302.507
# and so on.
# Write a program that prompts the user to enter a monthly saving amount and
# displays the account value after the sixth month.

monthlySavingAmount = eval(input("Enter monthly saving amount: "))
IR = 0.00417
total = monthlySavingAmount * (1 + IR)
total = (monthlySavingAmount + total) * (1 + IR)
total = (monthlySavingAmount + total) * (1 + IR)
total = (monthlySavingAmount + total) * (1 + IR)
total = (monthlySavingAmount + total) * (1 + IR)
total = (monthlySavingAmount + total) * (1 + IR)
print("The amount in account after 6 months is: ",total)