# Write the following function that returns true if the list is already
# sorted in increasing order:
# def isSorted(lst):
# Write a test program that prompts the user to enter a list and displays whether the
# list is sorted or not. Here is a sample run:

def isSorted(lst):
    for i in range(len(lst)):
        current = lst[i]
        for j in range(i+1, len(lst)):
            if current>lst[j]:
                return False
    return True

numbers = input("Enter ten numbers")
numList = [int(x) for x in numbers.split()]
print(isSorted(numList))

