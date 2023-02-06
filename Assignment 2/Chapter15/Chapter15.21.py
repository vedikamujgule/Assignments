# 15.21 (Binary to decimal) Write a recursive function that parses a binary number as a
# stringInputing into a decimal integer. The function header is as follows:
# def binaryToDecimal(binaryString):
# Write a test program that prompts the user to enter a binary stringInputing and displays its
# decimal equivalent.


def binaryToDecimal(binaryString):
    return binaryToDecimalHelper(binaryString, 0, 0)

def binaryToDecimalHelper(stringInput, dec, i):
    if stringInput != '':
        dec += int(stringInput[-1]) * 2 ** i
        return binaryToDecimalHelper(stringInput[:len(stringInput) - 1], dec, i + 1)
    return dec

print(binaryToDecimal(input("Enter binary string Input: ")))

# def btd(stringInput):
#     return btdhelper(stringInput,0,0)
# def btdhelper(stringInput,dec,i):
#     if stringInput != '':
#         dec += int(stringInput[-1])