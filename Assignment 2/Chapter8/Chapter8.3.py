# (Check password) Some Web sites impose certain rules for passwords. Write a
# function that checks whether a string is a valid password. Suppose the password
# rules are as follows:
# ■ A password must have at least eight characters.
# ■ A password must consist of only letters and digits.
# ■ A password must contain at least two digits.
# Write a program that prompts the user to enter a password and displays valid
# password if the rules are followed or invalid password otherwise.

def checkPassword(userInput):
    noOfCh = 0
    noOfDigits = 0
    for ch in userInput[:]:
        if ch.isdigit():
            noOfDigits +=1
        if ch.isalpha():
            noOfCh +=1
    if noOfDigits<2 or noOfCh<8:
        return False
    else: 
        return True

def main():
    userInput = input("Enter the password: \t")
    result = checkPassword(userInput)
    if result:
        print("The password is valid!")
    else:
        print("The password is invalid")

main()