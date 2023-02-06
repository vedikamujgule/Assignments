
# Write a program that prompts the user to enter the students’
# names and their scores on one line, and prints student names in increasing order
# of their scores. (Hint: Create a list. Each element in the list is a sublist with two
# elements: score and name. Apply the sort method to sort the list. This will sort
# the list on scores.)

lst = input("Enter name and marks of student's").split()
students = []
for i in range(0,len(lst),2):
    students.append([lst[i], lst[i+1]])

students.sort(key=lambda x:x[1])
print(students)

for i in students:
    print("Name: ", i[0], "\t")
    print("Score: ", i[1], "\n")

