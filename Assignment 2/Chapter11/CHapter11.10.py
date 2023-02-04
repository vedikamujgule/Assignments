# (Largest rows and columns) Write a program that randomly fills in 0s and 1s into
# a matrix, prints the matrix, and finds the rows and columns with the most
# 1s. Here is a sample run of the program:
# 0011
# 0011
# 1101
# 1010
# The largest row index: 2
# The largest column index: 2, 3

import random

def getRandBinaryValue():
    return random.randint(0, 1)

a4x4Matrix = []

index = 0
max = 0
count = 0

# Fill 4x4 Matrix and get largest row index in the process
for i in range(4):
    count = 0
    a4x4Matrix.append([0] * 4)
    for j in range(4):
        a4x4Matrix[i][j] = getRandBinaryValue()
        count = count + a4x4Matrix[i][j]
        if (count>max):
            max = count
            index = i


# Display 2D in matrix style
for i in range(4):
    for j in range(4):
        print(a4x4Matrix[i][j], end=" ")
        if(j==3):
            print()

# Finding largest col index
columnTraversed = 0
largestColumnIndex = 0
rowsTraversed = 0
currentColumnSum = 0
largestColumnSum = 0
while(columnTraversed<4):
    currentColumnSum = currentColumnSum + a4x4Matrix[rowsTraversed][columnTraversed]
    if(currentColumnSum>largestColumnSum):
        largestColumnIndex = columnTraversed
        largestColumnSum = currentColumnSum

    if(rowsTraversed == 3):
        columnTraversed+=1
        currentColumnSum = 0
        rowsTraversed=-1

    rowsTraversed += 1


print("The largest row index: " ,index)
print("The largest col index: ", largestColumnIndex, largestColumnSum)