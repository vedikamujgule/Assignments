# hapter10: 2, 3, 9, 15, 16, 18, 26, 36
# Reverse the numbers entered) Write a program that reads a list of integers and
# displays them in the reverse order in which they were read.

numbers = input("Enter digits seperated by space : ")
nums = [int(s) for s in numbers.split()]
res = nums[::-1]
print(res)
