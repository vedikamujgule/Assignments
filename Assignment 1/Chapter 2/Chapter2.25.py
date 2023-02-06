# (Turtle: draw a rectangle) Write a program that prompts the user to enter the
# center of a rectangle, width, and height, and displays the rectangle, as shown in
# Figure 2.4c.
import turtle
X,Y, w, h = eval(input("Enter center - X,center - Y, width , height: "))

turtle.penup()
turtle.goto(X - 0.5 * w, Y + 0.5 * h)
turtle.pendown()
turtle.forward(w)
turtle.right(90)
turtle.forward(h)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h)
turtle.done()  