# 13.1 (Remove text) Write a program that removes all the occurrences of a specified
# string from a text file. Your program should prompt the user to enter a filename
# and a string to be removed.

filename = input("Enter a filename: ").strip()
string = input("Enter the string to be removed: ")
file = open(filename, 'r')
data = ''
for line in file:
    data += line.replace(string, '')

resFile = open('Text', 'w')
resFile.write(data)
resFile.close()
print("Done")