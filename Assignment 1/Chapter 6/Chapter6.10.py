# Use the isPrime Function) Listing 6.7, PrimeNumberFunction.py, provides the
# isPrime(number) function for testing whether a number is prime. Use this
# function to find the number of prime numbers less than 10,000.

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

count = 0
for i in range(1, 10001):
    if  isPrime(i):
        count += 1

print("The number of prime numbers less than 10000 are: ", count)