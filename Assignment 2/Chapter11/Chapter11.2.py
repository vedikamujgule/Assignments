# # hapter11: 2, 5, 6, 10, 13, 25, 36, 51
# Sum the major diagonal in a matrix) Write a function that sums all the numbers
# of the major diagonal in an matrix of integers using the following header:
# def sumMajorDiagonal(m):
# The major diagonal is the diagonal that runs from the top left corner to the bottom
# right corner in the square matrix. Write a test program that reads a matrix and
# displays the sum of all its elements on the major diagonal. Here is a sample run:

def sumMajorDiagonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum

matrix = []
for i in range(4): 
    row = input("Enter a 4-by-4 matrix row for row " + str(i + 1) + ": ").split()
    matrix.append([float(x) for x in row])
    print(matrix)

print("Sum of the elements in the major diagonal is", sumMajorDiagonal(m))