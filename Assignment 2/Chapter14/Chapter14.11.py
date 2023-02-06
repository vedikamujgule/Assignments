# 14.11 (Count consonants and vowels) Write a program that prompts the user to enter a
# text filename and displays the number of vowels and consonants in the file. Use
# a set to store the vowels A, E, I, O, and U.

vowels = {'a', 'e', 'i', 'o', 'u'}
vowelsCount = 0
consonantsCount = 0
file = open(input("Enter filename: "))
lines = file.readlines()
for line in lines:
    for word in line.split():
        for ch in word.lower():
            if ch in vowels:
                vowelsCount += 1
            else:
                consonantsCount += 1

print("The Total number of vowels are :", vowelsCount)
print("The Total number of consonants are: ", consonantsCount)