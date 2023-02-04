# Use the isPrime Function) Listing 6.7, PrimeNumberFunction.py, provides the
# isPrime(number) function for testing whether a number is prime. Use this
# function to find the number of prime numbers less than 10,000.
count = 0
# def isPrime(number):
#     if number%2 == 0:
#         count += 1
#     return count

for i in range(0,10000):
    if i%2 == 0:
        count += 1
print(count)

#     count = 0
# for i in range(1, 10001):
#     if MyFunctions.isPrime(i):
#         count += 1

# print("The number of primes less than 10,000 is", count)