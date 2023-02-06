#(Turtle: draw points, rectangles, and circles) Use the functions defined in Listing
# to write a program that displays a rectangle centered at with width
# and height 100 and a circle centered at (50, 0) with radius 50. Fill 10 random
# points inside the rectangle and 10 inside the circle, as shown in Figure 6.11c.
# Draw a point at the specified location (x, y)

import random
import turtle


def drawPoint(x, y):
    turtle.penup()  
    turtle.goto(x, y)
    turtle.pendown()  
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()


# circle
def drawCircle(x, y, radius):
    turtle.penup()  
    turtle.goto(x, y - radius)
    turtle.pendown()  
    turtle.circle(radius)


# rectangle
def drawRectangle(x, y, width, height):
    turtle.penup()  
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()  
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)

def main():
    drawRectangle(-75, 0, 100, 100)
    drawCircle(50, 0, 50)
    for i in range(10):
        drawPoint(random.randint(-115,-30), random.randint(-50,40))
        drawPoint(random.randint(20, 90), random.randint(-40, 25))
    turtle.done()

main()