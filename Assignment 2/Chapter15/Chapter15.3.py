# 15.3 (Compute greatest common divisor using recursion) The gcd(m, n) can also be
# defined recursively as follows:
# ■ If m % n is 0, gcd(m, n) is n.
# ■ Otherwise, gcd(m, n) is gcd(n, m % n).
# Write a recursive function to find the GCD. Write a test program that prompts the
# user to enter two integers and displays their GCD.

def gcd(m, n):
    if m % n == 0:
        return n
    return gcd(n, m % n)

num1, num2 = eval(input("Enter two numbers: "))

print("The GCD of", num1, "and", num2, "is", gcd(num1,num2))