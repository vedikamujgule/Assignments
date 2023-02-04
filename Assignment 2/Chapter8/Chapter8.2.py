# (Check substrings) You can check whether a string is a substring of another string
# by using the find method in the str class. Write your own function to implement
# find. Write a program that prompts the user to enter two strings and then checks
# whether the first string is a substring of the second string.

def main():
    string1 = input("Enter the First String ")
    string2 = input("Enter the Second String ")
    result = find(string1, string2)
    if result ==-1:
        print("The first string is not a substring of the second string")
    else:
        print("The first string is a substring of the second string at index ", str(result))
    
def find(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    start = 0
    while len1<=len2:
        if s1 !=s2[start:start+len1]:
            start +=1
            len1 -+1
        else:
            return start
    return -1

main()

