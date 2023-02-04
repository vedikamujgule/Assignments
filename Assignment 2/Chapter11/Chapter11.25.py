# (Bubble sort) Write a sort function that uses the bubble-sort algorithm. The
# bubble-sort algorithm makes several passes through the list. On each pass,
# successive neighboring pairs are compared. If a pair is in decreasing order,
# its values are swapped; otherwise, the values remain unchanged. The technique
# is called a bubble sort or sinking sort because the smaller values gradually
# “bubble” their way to the top and the larger values “sink” to the bottom.
# Write a test program that reads in ten numbers, invokes the function, and displays
# the sorted numbers.

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
