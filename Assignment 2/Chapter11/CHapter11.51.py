lst = input("Enter students’ names and scores: ").split()

students = []

for i in range(0, len(lst), 2):
    students.append([lst[i], int(lst[i + 1])])

students.sort(key=lambda x: x[1])


for student in students:
    print(format(student[0], '8s'), end='')
    print(student[1])