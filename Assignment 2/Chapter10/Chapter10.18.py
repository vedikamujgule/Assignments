# The classic Eight Queens puzzle is to place eight
# queens on a chessboard such that no two queens can attack each other (i.e., no
# two queens are in the same row, same column, or same diagonal). There are
# many possible solutions. Write a program that displays one such solution. A
# sample output is shown below: 

def main():
    queens = 8 * [-1] 
    queens[0] = 0
    k = 1
    while k >= 0 and k <= 7:
        j = findPosition(k, queens)
        if j < 0:
            queens[k] = -1
            k -= 1  
        else:
            queens[k] = j
            k += 1
    printResult(queens)


def findPosition(k, queens):
    start = 0 if queens[k] == -1 else (queens[k] + 1)

    for j in range(start, 8):
        if isValid(k, j, queens):
            return j 
    return -1

# Return true if you a queen can be placed at (k, j)
def isValid(k, j, queens):
    # See if (k, j) is a possible position
    # Check jth column
    for i in range(k):
        if queens[i] == j:
            return False
    row = k - 1
    column = j - 1
    while row >= 0 and column >= 0:
        if queens[row] == column:
            return False
        row -= 1
        column -= 1
    row = k - 1
    column = j + 1
    while row >= 0 and column <= 7:
        if queens[row] == column:
            return False

        row -= 1
        column -= 1

    return True


def printResult(queens):
    for i in range(8):
        print(str(i) + ", " + str(queens[i]))
    print()
    for i in range(8):
        for j in range(queens[i]):
            print("| ", end="")
        print("|Q|", end="")

        for j in range(queens[i] + 1, 8):
            print(" |", end="")
        print()
main()