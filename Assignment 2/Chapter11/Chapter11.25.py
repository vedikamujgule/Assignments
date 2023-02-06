# (Markov matrix) An matrix is called a positive Markov matrix if each element
# is positive and the sum of the elements in each column is 1. Write the following
# function to check whether a matrix is a Markov matrix:

def isMarkovMatrix(matrix):
    for row in matrix:
        for ele in row:
            if ele < 0:
                return False
        if sum(row) != 1:
            return False
    return True

mat = []
print('Enter a 3*3 matrix:')
for i in range(3):
    x = input().split()
    x = [eval(r) for r in x]
    mat.append(x)

transpose = [[row[i] for row in mat] for i in range(len(mat[0]))]
if(isMarkovMatrix(transpose)):
    print("It's a markov matrix!")
else:
    print("It's not markov matrix")
