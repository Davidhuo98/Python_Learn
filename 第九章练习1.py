import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)  # 正值数据
y2 = -np.cos(x)  # 负值数据，我们将其取反以便在正y轴上显示

# 创建图形和轴
fig, ax1 = plt.subplots()

# 绘制第一个数据集
color = 'tab:red'
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)', color=color)
ax1.plot(x, y1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# 创建第二个y轴，并将其翻转和重新定位到下方
ax2 = ax1.twinx()
ax2.spines['bottom'].set_position(('outward', 60))  # 向下移动底部轴线
ax2.spines['top'].set_position(('outward', 40))  # 向上移动顶部轴线
ax2.spines['right'].set_color('none')  # 隐藏右侧轴线
ax2.yaxis.tick_right()  # 将y轴刻度移到右侧
ax2.yaxis.set_label_position('right')  # 将y轴标签移到右侧
ax2.set_ylabel('-cos(x)', color='tab:blue')
ax2.plot(x, y2, color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# 翻转y2轴
ax2.invert_yaxis()

# 调整布局
fig.tight_layout()

# 显示图形
plt.show()