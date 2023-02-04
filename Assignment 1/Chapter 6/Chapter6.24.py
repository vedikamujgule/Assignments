# (Palindromic prime) A palindromic prime is a prime number that is also palindromic.
# For example, 131 is a prime and also a palindromic prime, as are 313 and
# 757. Write a program that displays the first 100 palindromic prime numbers. Display
# 10 numbers per line and align the numbers properly, as follows:
# 2 3 5 7 11 101 131 151 181 191
# 313 353 373 383 727 757 787 797 919 929

def IsPalindrome(n):
    if int(str(n)[::-1]) == n:
        return True
    else:
        return False
def isPrime(n):
    if n%2 ==0:
        return True
    else:
        return False
counter=1
num = 2
while counter<101:
    if(isPrime(num) and IsPalindrome(num)):
        if counter % 10 != 0:
            print(num, end='  ')
        else:
            print(num)
        counter += 1
    num +=1

