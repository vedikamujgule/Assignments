#(Turtle: chessboard) Write a program to draw a chessboard, as shown in


import turtle
turtle.penup()
turtle.goto(-150, 120)
turtle.left(45)
turtle.pendown()
black = False
#run the loop 8 times per row ad col to get the 8*8 board
for i in range(1, 9):
    for j in range(1, 9):
        turtle.begin_fill()
        turtle.circle(30, steps=4)
        if black:
            turtle.color("black") #Fill black alternatively
            black = not black
        else:
            turtle.color("white") #Fill white alternatively
            black = not black
        turtle.end_fill()
        turtle.penup()
        turtle.goto(turtle.xcor() + 42, turtle.ycor())
        turtle.pendown()
    turtle.penup()
    turtle.goto(-150, turtle.ycor() - 42)
    turtle.pendown()
    black = not black
turtle.penup()
turtle.left(180)
turtle.goto(-192, 161)
turtle.color("black")  #Add black border to board with a thich pen size
turtle.pensize(3)
turtle.pendown()
turtle.circle(240, steps=4)
turtle.done()