# 4.15 (Game: lottery) Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
# number. The program prompts the user to enter a three-digit number and determines
# whether the user wins according to the following rules:
# 1. If the user input matches the lottery number in the exact order, the award is
# $10,000.
# 2. If all the digits in the user input match all the digits in the lottery number, the
# award is $3,000.
# 3. If one digit in the user input matches a digit in the lottery number, the award is
# $1,000.

import random

NUM = int(random.randint(100,999))
print(NUM)
USER = eval(input("Enter a 3 digit number"))

num = NUM
user = USER
user1 = user//100
user = user%100
user2 = user//10
user = user%10
user3 = user

num1 = num//100
num = num%100
num2 = num//10
num = num%10
num3 = num

if USER == NUM:
    print(USER, NUM)
    print("The award is $10,000.")
elif (user1 == num1 and user2 == num3 and user3==num2 or 
      user1 == num2 or user2 == num2 or user3==num2 and 
      user1 == num3 or user2 == num3 or user3==num3):
    print("The award is $3,000.")
elif (user1 == num1 or user2 == num1 or user3==num1 or 
      user1 == num2 or user2 == num2 or user3==num2 or 
      user1 == num3 or user2 == num3 or user3==num3):
    print("The award is $1,000.")
else:
    print("Sorry! No award for you.")
