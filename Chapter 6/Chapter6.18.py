# (Display matrix of 0s and 1s) Write a function that displays an n-by-n matrix using
# the following header:
# def printMatrix(n):
# Each element is 0 or 1, which is generated randomly. Write a test program that
# prompts the user to enter n and displays an n-by-n matrix. Here is a sample run:

import random
def printMatrix(n):
    for i in range(0,n*n+1):
        x = random.randint(0,1)
        print(x,end=" ")
        if(i%n ==0):
            print("")

n = eval(input("Enter a number"))
printMatrix(n)