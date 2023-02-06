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

result =[]
# iterate through rows of m1    
for i in range(len(m1)):
    result.append([0]*3)
    # iterating by column by m2
    for j in range(len(m2[0])):
        # iterating by rows of m2
        for k in range(len(m2)):
            result[i][j] += m1[i][k] * m2[k][j]
            
print("The Matrices are multiplied as follows: ")

# Display 2D in matrix style
for i in range(3):
    for j in range(3):
        print(result[i][j], end=" ")
        if(j==2):
            print()