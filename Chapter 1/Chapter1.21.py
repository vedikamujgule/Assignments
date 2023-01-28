# (Turtle: display a clock) Write a program that displays a clock to show the time
# 9:15:00, as shown in Figure 1.20c.

import turtle
turtle.pendown()
turtle.left(90)
turtle.pensize(3)
turtle.forward(70)
turtle.penup()
turtle.left(180)
turtle.pensize(1)
turtle.forward(70)
turtle.right(90)
turtle.pendown()
turtle.forward(40)
turtle.penup()
turtle.right(180)
turtle.forward(40)
turtle.pensize(2)
turtle.pendown()
turtle.forward(50)
turtle.right(180)
turtle.penup()
turtle.forward(50)
turtle.goto(0,100)
turtle.pendown()
turtle.circle(100)

 # label
turtle.write(str(12), align="center",
              font=("Arial",
                    12, "normal"))

turtle.left(90)
turtle.penup()
turtle.forward(220)
turtle.write(str(6), align="center",
              font=("Arial",
                    12, "normal"))
turtle.left(180)
turtle.penup()
turtle.forward(100)
turtle.right(90)
turtle.forward(110)
turtle.write(str(3), align="center",
              font=("Arial",
                    12, "normal"))
turtle.left(180)
turtle.penup()
turtle.forward(220)
turtle.write(str(9), align="center",
              font=("Arial",
                    12, "normal"))

