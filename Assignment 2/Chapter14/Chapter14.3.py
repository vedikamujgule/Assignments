# 14.3 (Count the occurrences of each keyword) Write a program that reads in a Python
# source code file and counts the occurrence of each keyword in the file. Your program
# should prompt the user to enter the Python source code filename.

import os.path
import sys

def main():
    keyWordsArray = {"and": 0, "as": 0, "assert": 0, "break": 0, "class": 0,
                "continue": 0, "def": 0, "del": 0, "elif": 0, "else": 0,
                "except": 0, "False": 0, "finally": 0, "for": 0, "from": 0,
                "global": 0, "if": 0, "import": 0, "in": 0, "is": 0, "lambda": 0,
                "None": 0, "nonlocal": 0, "not": 0, "or": 0, "pass": 0, "raise": 0,
                "return": 0, "True": 0, "try": 0, "while": 0, "with": 0, "yield": 0}

    filename = input("Enter a Python source code filename: ").strip()

    if not os.path.isfile(filename):
        print("File with name", filename, "does not exist")
        sys.exit()
    infile = open(filename, "r")
    text = infile.readlines()
    for i in range(len(text)):
        indx = text[i].find(chr(35))
        if indx != -1:
            line = text[i]
            line = line[0:indx]
            text[i] = line
    for line in text:
        for word in line.split():
            if word in keyWordsArray:
                keyWordsArray[word] += 1

    for item in keyWordsArray:
        print(item, ":", keyWordsArray[item])

main()