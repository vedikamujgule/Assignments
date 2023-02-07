# Locate the largest element) Write the following function that returns the location
# of the largest element in a two-dimensional list:
# def locateLargest(a):
# The return value is a one-dimensional list that contains two elements. These
# two elements indicate the row and column indexes of the largest element in the
# two-dimensional list. Write a test program that prompts the user to enter a twodimensional
# list and displays the location of the largest element in the list. Here is
# a sample run:
import random

def getRandBinaryValue():
    return random.randint(0, 1)

a4x4Matrix = []

# Fill 4x4 Matrix and get largest row index in the process
for i in range(4):
    a4x4Matrix.append([0] * 4)
    for j in range(4):
        a4x4Matrix[i][j] = getRandBinaryValue()


listSums = [sum(r) for r in a4x4Matrix]

max1 = max(listSums)


indexCollection = []

for i in range(len(listSums)):
    if listSums[i] == max1:
        indexCollection.append(i)

print(indexCollection)

# Display 2D in matrix style
for i in range(4):
    for j in range(4):
        print(a4x4Matrix[i][j], end=" ")
        if(j==3):
            print()

print("The largest row index", end=" ")
print(*indexCollection, sep=", ")