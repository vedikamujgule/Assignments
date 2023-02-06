# (The Location class) Design a class named Location for locating a maximal
# value and its location in a two-dimensional list. The class contains the public data
# fields row, column, and maxValue that store the maximal value and its indexes in
# a two-dimensional list, with row and column as int types and maxValue as a
# float type.
# Write the following method that returns the location of the largest element in a
# two-dimensional list.
# def Location locateLargest(a):
# The return value is an instance of Location. Write a test program that prompts
# the user to enter a two-dimensional list and displays the location of the largest element
# in the list. Here is a sample run:

class Location:
    def __init__(self):
        self.row =-1
        self.col = -1
        self.maxValue = -1
    
def getLocation(lst):
        loc = Location()

        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j]>loc.maxValue:
                    loc.row = i
                    loc.col = j
                    loc.maxValue = lst[i][j]
        return loc
    
def main():
    row, col = eval(input("Enter the number of rows and colums in the list"))
    lst =[]

    for i in range(row):
        row = input("Enter row data: ").split()
        row = [int(x) for x in row]
        lst.append(row)
    loc = getLocation(lst)

    print("The largest element "+ str(loc.maxValue) + " is at location "+ str(loc.row),str(loc.col))

main()

