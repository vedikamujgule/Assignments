# (Palindrome integer) Write the functions with the following headers:
# # Return the reversal of an integer, e.g. reverse(456) returns
# # 654
# def reverse(number):
# # Return true if number is a palindrome
# def isPalindrome(number):
# Use the reverse function to implement isPalindrome. A number is a palindrome
# if its reversal is the same as itself. Write a test program that prompts the
# user to enter an integer and reports whether the integer is a palindrome.

reversedNo = 0
def reverse(number):
    reversedNo = (str)(number)[::-1]
    return int(reversedNo)

def isPalindrome(number):
    if number == reverse(number):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

number = eval(input("Enter a number"))
print(isPalindrome(number))