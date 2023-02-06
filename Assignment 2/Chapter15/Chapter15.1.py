# 15.1 (Sum the digits in an integer using recursion) Write a recursive function that computes
# the sum of the digits in an integer. Use the following function header:
# def sumDigits(n):
# For example, sumDigits(234) returns Write a test program
# that prompts the user to enter an integer and displays its sum.


def sumDigits(num):
    if num == 0:
        return num
    return (num % 10 + sumDigits(num//10))

userInput = eval(input("Enter a digit: "))
print("The sum of the digits is:", sumDigits(userInput))
