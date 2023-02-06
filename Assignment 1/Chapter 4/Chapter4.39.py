# 4.39 (Turtle: two circles) Write a program that prompts the user to enter the center
# coordinates and radii of two circles and determines whether the second circle is
# inside the first or overlaps with the first, as shown in Figure 4.16.
import math
import turtle

x1, y1, r1 = eval(input("Enter circle1's center x-coordinate, y-coordinates, and radius: "))
x2, y2, r2 = eval(input("Enter circle2's center x-coordinate, y-coordinates, and radius: "))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.circle(r1)

turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.circle(r2)

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

turtle.penup()
turtle.goto(max(x1 + r1, x2 + r2), max(y1 + r1, y2 + r2))
turtle.pendown()

if distance <= abs(r1 - r2):
    turtle.write("circle 2 inside circle 1")
elif distance <= r1 + r2:
    turtle.write("circle 2 overlaps circle 1")
else:
    turtle.write("circle 2 does not overlap circle 1")

turtle.done()