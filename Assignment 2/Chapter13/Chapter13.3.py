# 13.3 (Process scrs in a text file) Suppose that a text file contains an unspecified number
# of scrs. Write a program that reads the scrs from the file and displays their
# total and average. Scores are separated by blanks. Your program should prompt
# the user to enter a filename.

filename = input("Enter filename: ").strip()
file = open(filename, 'r')
#initalize vaiables
count = 0
average = 0
sum = 0
for line in file:
    scrs = line.split()
    scrs = [eval(s) for s in scrs]
    count += len(scrs)
    for s in scrs:
        sum += s

average = sum / count

print("There are total: ", count, "scores in the file")
print("The total sum is: ", sum)
print("The average is: ", average)