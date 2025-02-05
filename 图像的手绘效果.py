from PIL import Image
import numpy as np

# 初始化法线向量的e1分量，单位为弧度
vec_e1 = np.pi / 2.2
# 初始化法线向量的az分量，单位为弧度
vec_az = np.pi / 4
# 初始化深度值
depth = 10.

# 打开图像文件并转换为灰度模式
im = Image.open('C:/Users/WOOKING/Desktop/R-C.jpg').convert('L')
# 将图像转换为numpy数组，数组类型为浮点数
a = np.asarray(im).astype('float')
# 计算灰度图像的梯度
grad = np.gradient(a)
# 分别取横纵图像的梯度值
grad_x, grad_y = grad
# 根据深度值调整梯度分量
grad_x = grad_x * depth / 100. #添加小数点是为了清晰地表明数字应该被视为具有潜在的小数部分，即使该部分实际为零
grad_y = grad_y * depth / 100.
# 计算法线向量的dx, dy, dz分量
dx = np.cos(vec_e1) * np.cos(vec_az)
dy = np.cos(vec_e1) * np.sin(vec_az)
dz = np.sin(vec_az)
'''
为了计算法线向量的笛卡尔坐标分量（dx, dy, dz），需要使用以下公式：
dx = r * sin(θ) * cos(φ)
dy = r * sin(θ) * sin(φ)
dz = r * cos(θ)
在这个例子中，r（向量的长度）通常设为1，因为通常我们关心的是方向而不是长度。所以，实际上计算的是单位法线向量的笛卡尔坐标分量。
'''
# 计算归一化后的法线向量分量
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A
# 计算最终的像素值
a2 = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
# 确保像素值在0-255之间
a2 = a2.clip(0, 255)
# 从数组创建图像对象
im2 = Image.fromarray(a2.astype('uint8'))
# 保存处理后的图像
im2.save('故宫手绘效果图.jpg')
