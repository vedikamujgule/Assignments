# 5.36 (Game: scissor, rock, paper) Programming Exercise 4.17 gives a program that
# plays the scissor, rock, paper game. Revise the program to let the user play continuously
# until either the user or the computer wins more than two times.

import random

count = 0
while count <= 2 or count <= -2:
    computerNumber = random.randint(0, 2)
    userNumber = eval(input("rock (0), paper (1), scissor (2): "))
    if computerNumber == 0:
        if userNumber == 0:
            print("It's a draw")
        elif userNumber == 1:
            print("You won!!")
            count += 1
        elif userNumber == 2:
            print("You lost")
            count -= 1
    elif computerNumber == 1:
        if userNumber == 0:
            print("You lost")
            count -= 1
        elif userNumber == 1:
            print("It's a draw!!")
        elif userNumber == 2:
            print("You won!!")
            count += 1
    elif computerNumber == 2:
        if userNumber == 0:
            print("You won")
            count += 1
        elif userNumber == 1:
            print("You lost")
            count -= 1
        elif userNumber == 2:
            print("It's a draw!!")

if count > 2:
    print("You won more than two times!")
else:
    print("The computer won more than two times..")