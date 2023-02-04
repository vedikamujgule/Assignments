# (Algebra: multiply two matrices) Write a function to multiply two matrices. The
# header of the function is:
# def multiplyMatrix(a, b)
# To multiply matrix a by matrix b, the number of columns in a must be the same as
# the number of rows in b, and the two matrices must have elements of the same or
# compatible types. Let c be the result of the multiplication. Assume the column size
# of matrix a is n. Each element is For
# example, for two matrices a and b, c is
# where
# Write a test program that prompts the user to enter two matrices and displays
# their product. Here is a sample run:
# 3 * 3
# cij = ai1 * b1j + ai2 * b2j + ai3 * b3j.
# = £
# c11 c12 c13
# c21 c22 c23
# c31 c32 c33
# £ ≥
# a11 a12 a13
# a21 a22 a23
# a31 a32 a33
# ≥ * £
# b11 b12 b13
# b21 b22 b23
# b31 b32 b33
# ≥
# 3 * 3
# ai1 * b1j + ai2 * b2j + c cij + ain * bnj.
# Enter matrix1:

l1 = input("Enter matrix 1: ").split()
l2 = input("Enter matrix 2: ").split()

# shape the input into a 3*3 matrix
m1 = []
m2 = []
counter = 0
for i in range(3):
    m1.append([0] * 3)
    m2.append([0] * 3)
    for j in range(3):
        m1[i][j] = float(l1[counter])
        m2[i][j] = float(l2[counter])
        counter += 1


product = []
cellValue = 0
# Multiply the matrices and store result in sum
# Take each row of M1 against ever col of M2

for i in range(3):
    product.append([0] * 3)
    j=0
    CurrentM1Column = 0
    while(CurrentM1Column!=3):
        cellValue += m1[i][j]*m2[j][CurrentM1Column] #compare every row of M1 against every column of M2, counter points to the current M2 col

        if((j+1)%3==0 and CurrentM1Column <3):   #after every row
            product[i][CurrentM1Column] = round(cellValue,2)
            cellValue = 0
            CurrentM1Column += 1
            j=-1  # resetting to -1, so after J+=1, j = 0 ==> reset
        j += 1

print("The Matrices are added as follows: ")

# Display 2D in matrix style
for i in range(3):
    for j in range(3):
        print(product[i][j], end=" ")
        if(j==2):
            print()