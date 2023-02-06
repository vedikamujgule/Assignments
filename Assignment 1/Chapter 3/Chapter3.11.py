# (Reverse number) Write a program that prompts the user to enter a four-digit integer
# and displays the number in reverse order.

no = eval(input("Enter a four digit number: "))
num1 = no%10
no //=10
num2 = no%10
no //=10
num3 = no%10
no //=10
num4 = no%10
print(num1, num2, num3,num4)
