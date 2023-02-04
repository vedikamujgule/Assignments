
# *5.26 (Sum a series) Write a program to sum the following series:
sum = 0
for i in range(1,99):
    if(i%2 !=0):
        sum += i/(i+2)
print(sum)
