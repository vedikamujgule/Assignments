# (Statistics: compute deviation) Exercise 5.46 computes the standard deviation of
# numbers. This exercise uses a different but equivalent formula to compute the
# standard deviation of n numbers.
# To compute the standard deviation with this formula, you have to store the
# individual numbers using a list, so that they can be used after the mean is
# obtained.
# Your program should contain the following functions:
# # Compute the standard deviation of values
# def deviation(x):
# # Compute the mean of a list of values
# def mean(x):
# Write a test program that prompts the user to enter a list of numbers and displays
# the mean and standard deviation, as shown in the following sample run:

import math

def deviation(x):
    meanValue = mean(x)
    print("The mean value is "+ format(meanValue,'.2f'))
    a = [(i-meanValue)**2 for i in x]
    sum(a)
    deviation = math.sqrt((sum(a)/len(x)-1))
    return deviation

def mean(x):
    return sum(x)/len(x)

def main():
    numbers = input("Enter the numbers with a space")
    resDeviation = deviation([float(s) for s in numbers.split()])
    print("The deviation value is "+ format(resDeviation,'.5f'))

main()