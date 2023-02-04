# Write a program that prompts the user to enter the
# number of students and each student’s score, and displays the highest and secondhighest scores

maxScore1 = 0
maxScore2 = -1
numberOfStudents = eval(input("Enter number of students"))

for i in range(0,numberOfStudents):
    score = eval(input("Enter Score"))
    if maxScore1 < score:
        maxScore1 = score
    if score<maxScore1 and score>maxScore2:
        maxScore2 = score

print("Top Student is with score", maxScore1)
print("The 2nd Top student with score", maxScore2)