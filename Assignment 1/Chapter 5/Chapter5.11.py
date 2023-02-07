# Write a program that prompts the user to enter the
# number of students and each student’s score, and displays the highest and secondhighest scores

ms1 = 0
ms2 = -1
numberOfStudents = eval(input("Enter number of students: "))

for i in range(0,numberOfStudents):
    score = eval(input("Enter Score: "))
    if ms1 < score:
        ms1 = score
    if score<ms1 and score>ms2:
        ms2 = score

print("Top Student is with score", ms1)
print("The student with 2nd nighest scode is", ms2)