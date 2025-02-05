import turtle
turtle.setup(400,400,300,300)
turtle.pensize(1)
for i in range(9):
    turtle.circle(30+(i-1)*20)
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(20)
    turtle.seth(0)
    turtle.pendown()
turtle.done()

