import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
X = np.array([0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6])  # 提供x轴坐标值
Y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])  # 提供y轴坐标值
print('X', X)
print('Y', Y)
plt.plot(X, Y, color='green')  # 绘制方波折线
plt.title('绘制方波折线', fontsize=20)
plt.show()  # 显示方波折线

