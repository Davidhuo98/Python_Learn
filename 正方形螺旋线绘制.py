# 绘制正方形螺旋线
from turtle import *

speed(0)  # 调节画笔速度
pensize(3)
pencolor("green")  # 画笔颜色
for i in range(60):  # 利用for循环画出正方形螺旋线
    seth(90 * i + 90)  # 改变画笔方向
    fd(10 + 5 * i)  # 改变画线长度
done()