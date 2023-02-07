
# 13.2 (Count characters, words, and lines in a file) Write a program that will count the
# number of characters, words, and lines in a file. Words are separated by a whitespace
# character. Your program should prompt the user to enter a filename.


##note: please create a file.checl for the coorect file

filename = input("Enter a filename: ").strip()
file = open(filename, 'r')

#initialize the variables
lines = 0
words = 0
chars = 0

for line in file:
    lines += 1
    words += len(line.split())
    for c in line:
        if c != ' ':
            chars += 1
            
#print variables
print(chars, ": no of characters")
print(words, ": no of words")
print(lines, ": no of Lines")