
# 6.29 (Financial: credit card no validation) Credit card numbers follow certain
# patterns: It must have between 13 and 16 digits, and the no must start with:

def isValid(no):
    if getSize(no) >= 13 and getSize(no) <= 16:
        if checkPrefixMatch(no, 4) or checkPrefixMatch(no, 5) or \
                checkPrefixMatch(no, 6) or getPrefix(no, 2) == 37:
            return True if (sumOfDoubleEvenPlace(no) +
                            sumOfOddPlace(no)) % 10 == 0 else False

def sumOfDoubleEvenPlace(no):
    noLst = []
    oddPlaceNoList = []
    for i in range(len(list(str(no)))):
        noLst.append(int(list(str(no))[i]))
    noLst.reverse()
    for j in range(1, len(noLst), 2):
        oddPlaceNoList.append(noLst[j])
    doubleOddPlaceNo = [i * 2 for i in oddPlaceNoList]
    digitOddPlaceNo = [getDigit(i) for i in doubleOddPlaceNo]
    return sum(digitOddPlaceNo)

def sumOfOddPlace(no):
    noLst = []
    totalNo = 0
    for i in range(len(list(str(no)))):
        noLst.append(int(list(str(no))[i]))
    noLst.reverse()
    for j in range(0, len(noLst), 2):
        totalNo += noLst[j]
    return totalNo

def getDigit(no):
    noLst = []
    for i in range(len(list(str(no)))):
        noLst.append(int(list(str(no))[i]))
    return sum(noLst)

def checkPrefixMatch(no, d):
    return True if int(str(no)[0]) == d else False

def getSize(no):
    return len(str(no))

def getPrefix(no, k):
    if len(str(no)) <= k:
        return no
    else:
        return int(str(no)[0:k])

def main():
    num = eval(input("Enter your credit card no: "))
    print(isValid(num))

main()