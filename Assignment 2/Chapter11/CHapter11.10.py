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

m1 = []
index = 0
max = 0
count = 0
indexCol =[]
# Fill 4x4 Matrix and get largest row index in the process
for i in range(4):
    count = 0
    m1.append([0] * 4)
    for j in range(4):
        m1[i][j] = getRandBinaryValue()
        count = count + m1[i][j]
        if (count>max):
            max = count
            index = i
print("row",index)

max = 0
transpose = [[row[i] for row in m1] for i in range(len(m1[0]))]
for i in range(4):
    for j in range(4):
        count = count + transpose[i][j]
        if (count>max):
            max = count
            indexCol = i
print("col",indexCol)

# Display 2D in matrix style
for i in range(4):
    for j in range(4):
        print(m1[i][j], end=" ")
        if(j==3):
            print()

# Finding largest col index
colVisited = 0
maxColIndex = 0
rowVisited = 0
currColSum = 0
maxColSum = 0
while(colVisited<4):
    currColSum = currColSum + m1[rowVisited][colVisited]
    if(currColSum>maxColSum):
        maxColIndex = colVisited
        maxColSum = currColSum

    if(rowVisited == 3):
        colVisited+=1
        currColSum = 0
        rowVisited=-1
    rowVisited += 1

print("The largest row index: " ,index)
print("The largest col index: ", maxColIndex, maxColSum)