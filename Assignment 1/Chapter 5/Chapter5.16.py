# 5.16 (Compute the greatest common divisor) For Listing 5.8, another solution to find
# the greatest common divisor of two integers n1 and n2 is as follows: First find d to
# be the minimum of n1 and n2, and then check whether d, d - 1, d - 2, ..., 2, or
# 1 is a divisor for both n1 and n2 in this order. The first such common divisor is the
# greatest common divisor for n1 and n2.

n1 = int(input("Enter 1st integer: "))
n2 = int(input("Enter nnd integer: "))

d = min(n1, n2)

while True:
    if n1 % d == 0 and n2 % d == 0:
        break
    d -= 1

print("The greatest common divisor (GCD) is: ", d)