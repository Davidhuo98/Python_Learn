import turtle
def koch(size,n):
    if n == 0:
        turtle.forward(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level = 5    # level 参数通常用于指定递归的深度，即图形的复杂程度
    koch(400,level)   #作为递归基例
    turtle.right(120)
    koch(400,level)   #作为递归基例
    turtle.right(120)
    koch(400, level)  #作为递归基例
    turtle.hideturtle()
main()
turtle.done()
