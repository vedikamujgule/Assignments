# (Turtle: draw shapes) Write a program that draws a triangle, square, pentagon,
# hexagon, and octagon, as shown in Figure 3.6b. Note that the bottom edges of
# these shapes are parallel to the x-axis. (Hint: For a triangle with a bottom line
# parallel to the x-axis, set the turtle’s heading to 60 degrees.)

import turtle

turtle.penup()
turtle.backward(200)

# triangle
turtle.pendown()
turtle.left(60)
turtle.begin_fill()
turtle.color("gray")
turtle.circle(70, steps=3)
turtle.end_fill()

#add space
turtle.penup()
turtle.setheading(0)
turtle.forward(130)

# square
turtle.pendown()
turtle.left(45)
turtle.begin_fill()
turtle.color("gray")
turtle.circle(70, steps=4)
turtle.end_fill()
#add space
turtle.penup()
turtle.setheading(0)
turtle.forward(130)

# pentagon
turtle.pendown()
turtle.left(35)
turtle.begin_fill()
turtle.color("gray")
turtle.circle(70, steps=5)
turtle.end_fill()

#add space
turtle.penup()
turtle.setheading(0)
turtle.forward(140)

# hexagon
turtle.pendown()
turtle.left(30)
turtle.begin_fill()
turtle.color("gray")
turtle.circle(70, steps=6)
turtle.end_fill()

#add space
turtle.penup()
turtle.setheading(0)
turtle.forward(50)

# octagon
turtle.pendown()
turtle.right(23)
turtle.begin_fill()
turtle.color("gray")
turtle.circle(40, steps=8)
turtle.end_fill()
turtle.done()

