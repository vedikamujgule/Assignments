# (Sort three numbers) Write the following function to display three numbers in
# increasing order:
# def displaySortedNumbers(num1, num2, num3):
# Write a test program that prompts the user to enter three numbers and invokes the
# function to display them in increasing order. Here are some sample runs:

def displaySortedNumbers(num1, num2, num3):
    if num1>num2:
        num1,num2 = num2,num1
    if num1>num3:
        num1,num3 = num3,num1
    if num2>num3:
        num2,num3 = num3,num2
    print("The sorted number are: ", num1, num2, num3)

num1,num2,num3 = eval(input("Enter 3 numbers: "))
displaySortedNumbers(num1,num2,num3)