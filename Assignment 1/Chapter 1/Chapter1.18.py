# (Turtle: draw a star) Write a program that draws a star, as shown in Figure 1.19c.
# (Hint: The inner angle of each point in the star is 36 degrees.)

import turtle
# turtle.pendown()
# turtle.left(36)
# turtle.forward(90)
# turtle.right(144)
# turtle.forward(90)
# turtle.right(144)
# turtle.forward(90)
# turtle.right(144)
# turtle.forward(90)
# turtle.right(144)
# turtle.forward(90)

# side = eval(input("Enter side"))
for i in range(5):
    turtle.pendown()
    turtle.forward(100)
    turtle.right(144)
turtle.done()

