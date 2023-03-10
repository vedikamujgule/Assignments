# (Simulation using Turtle: self-avoiding random walk) A self-avoiding walk in a
# lattice is a path from one point to another that does not visit the same point twice.
# Self-avoiding walks have applications in physics, chemistry, and mathematics.
# They can be used to model chainlike entities such as solvents and polymers. Write
# a Turtle program that displays a random path that starts from the center and ends at
# a point on the boundary, as shown in Figure 11.11a, or ends at a dead-end point
# (i.e., surrounded by four points that have already been visited), as shown in Figure
# 11.11b. Assume the size of the lattice is 16 * 16.

import turtle
from random import random
turtle.color("black")
N = 16
x = -80
i = (N + 1) // 2
j = (N + 1) // 2

for y in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(160)

y = 80
turtle.right(90)
for x in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(160)

lattice = []
for i in range(N):
    list = N * [False]
    lattice.append(list)
    
lattice[i][j] = True

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.setheading(0)

turtle.pensize(3)
turtle.color("black")
while i > 0 and i < N - 1 and j > 0 and j < N - 1:
    if lattice[i][j + 1] and lattice[i][j - 1] and lattice[i - 1][j] and lattice[i + 1][j]:
        break

    r = random()
    if r < .25 and not lattice[i][j + 1]:
        lattice[i][j + 1] = True
        j += 1
        turtle.setheading(0)
        turtle.forward(10)
    elif r < .50 and not lattice[i - 1][j]:
        lattice[i - 1][j] = True
        i -= 1
        turtle.setheading(270)
        turtle.forward(10)
    elif r < .75 and not lattice[i][j - 1]:
        lattice[i][j - 1] = True
        j -= 1
        turtle.setheading(180)
        turtle.forward(10)
    elif r < 1.00 and not lattice[i + 1][j]:
        lattice[i + 1][j] = True
        i += 1
        turtle.setheading(90)
        turtle.forward(10)

turtle.hideturtle()
turtle.done()