import turtle
def koch(size,n):
    if n == 0:
        turtle.forward(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.right(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(800,600)
    turtle.speed(0)  # 控制绘制速度,设置Turtle画笔的移动速度为最快，使得绘图过程尽可能快地完成
    turtle.penup()
    turtle.goto(-300,-50)  #将画笔移动到距离画布中心左侧300个单位、下方50个单位的位置
    turtle.pendown()
    turtle.pensize(2)
    turtle.color("red")
    koch(600,3)   # 0阶科赫曲线长度，阶数
    turtle.hideturtle()
main()
turtle.done()