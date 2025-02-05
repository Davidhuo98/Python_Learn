import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,6,100) #linspace函数，用于在指定范围内生成一组等差数列,该函数生成一个包含100个元素的数组，数组中的元素从0开始，以0.06的步长递增，直到6为止
y = np.cos(2*np.pi*x)*np.exp(-x)+0.8 #使用numpy库的cos函数计算2πx的余弦值，并将其与e的-x次方相乘,然后，它将结果与0.8相加
plt.plot(x,y,'k',color='r',linewidth=3,linestyle="-") # inestyle="-"表示线条样式为实线
plt.show()