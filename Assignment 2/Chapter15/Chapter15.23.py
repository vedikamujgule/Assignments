# 15.23 (String permutation) Write a recursive function to print all the permutations of a
# string. For example, for the string abc, the printout is:
# abc
# acb
# bac
# bca
# cab
# cba
# (Hint: Define the following two functions. The second function is a helper function.
# def displayPermuation(s):
# def displayPermuationHelper(string1, string2):
# The first function simply invokes displayPermuation(" ", s). The second
# function uses a loop to move a character from string2 to string1 and recursively invokes
# it with a new string1 and string2. The base case is that string2 is empty and prints string1 to the
# console.)
# Write a test program that prompts the user to enter a string and displays all its permutations.

def displayPermuation(s):
    displayPermuationHelper("", s)

def displayPermuationHelper(string1, string2):
    if string2 == '':
        print(string1)
    else:
        for i in range(len(string2)):
            displayPermuationHelper(string1 + string2[i], string2[0:i] + string2[i + 1:len(string2)])

displayPermuation(input("Enter a string: "))