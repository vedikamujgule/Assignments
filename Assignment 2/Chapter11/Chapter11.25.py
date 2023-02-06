# (Markov matrix) An matrix is called a positive Markov matrix if each element
# is positive and the sum of the elements in each column is 1. Write the following
# function to check whether a matrix is a Markov matrix:

def isMarkovMatrix(m):
    for row in m:
        for e in row:
            if e < 0:
                return False
        if sum(row) != 1:
            return False

    return True
mat = []
print('Enter a 3-by-3 matrix row by row:')
for i in range(3):
    x = input().split()
    x = [eval(r) for r in x]
    mat.append(x)


transpose = [[row[i] for row in mat] for i in range(len(mat[0]))]
print(transpose)
if(isMarkovMatrix(transpose)):
    print("It is a markov matrix")
else:
    print("It is not markov matrix")
