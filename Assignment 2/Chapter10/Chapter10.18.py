# The classic Eight Queens puzzle is to place eight
# qs on a chessboard such that no two qs can attack each other (i.e., no
# two qs are in the same row, same col, or same diagonal). There are
# many possible solutions. Write a program that displays one such solution. A
# sample output is shown below: 

#find position 
def findPosition(k, qs):
    start = 0 if qs[k] == -1 else (qs[k] + 1)

    for j in range(start, 8):
        if isValid(k, j, qs):
            return j 
    return -1

#check validity for the position
def isValid(k, j, qs):
    for i in range(k):
        if qs[i] == j:
            return False
    row = k - 1
    col = j - 1
    while row >= 0 and col >= 0:
        if qs[row] == col:
            return False
        row -= 1
        col -= 1
    row = k - 1
    col = j + 1
    while row >= 0 and col <= 7:
        if qs[row] == col:
            return False
        row -= 1
        col -= 1
    return True

#display function 
def printResult(qs):
    for i in range(8):
        print(str(i) + ", " + str(qs[i]))
    print()
    for i in range(8):
        for j in range(qs[i]):
            print("| ", end="")
        print("|Q|", end="")

        for j in range(qs[i] + 1, 8):
            print(" |", end="")
        print()


def main():
    qs = 8 * [-1] 
    qs[0] = 0
    k = 1
    while k >= 0 and k <= 7:
        j = findPosition(k, qs)
        if j < 0:
            qs[k] = -1
            k -= 1  
        else:
            qs[k] = j
            k += 1
    printResult(qs)
main()