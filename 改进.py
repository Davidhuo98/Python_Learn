import turtle

# 创建一个新的turtle对象
t = turtle.Turtle()

# 设置画笔速度和填充颜色
t.speed(1)
t.fillcolor("blue")

# 开始填充颜色
t.begin_fill()

# 绘制圆角正方形的上半部分
for _ in range(2):
    t.forward(100)  # 假设正方形的边长为100
    t.circle(20, 180)  # 绘制半径为20的圆角，角度为180度
    t.right(90)  # 右转90度

# 绘制圆角正方形的下半部分，但这次不填充颜色
t.penup()  # 提起笔，移动到正确的起始位置
t.goto(-50, -20)  # 假设这是下半部分的起始点（基于之前的绘制）
t.pendown()  # 放下笔开始绘制

for _ in range(2):
    t.forward(100)
    t.circle(20, 180)
    t.right(90)

# 结束填充颜色
t.end_fill()

# 隐藏turtle图标
t.hideturtle()

# 完成绘制，保持窗口打开
turtle.done()