import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
radar_labels = np.array(['研究型（I）', '艺术型（A）', '社会型（S）', '企业型（E）', '常规型（C）', '现实型（R）'])
nAttr = 6
data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
                 [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                 [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                 [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
                 [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
                 [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]])
data_labels = np.array(['工程师', '实验员', '艺术家', '推销员', '社会工作者', '记事员'])
angles = np.linspace(0,2*np.pi,nAttr,endpoint=False)
data = np.concatenate((data,[data[0]]))
angles = np.concatenate((angles,[angles[0]]))
fig = plt.figure(facecolor="white") #创建了一个背景颜色为白色的图形对象，用于后续在其中绘制图表或其他图形元素。
plt.subplot(111,polar=True) # polar=True参数表示这个子图是极坐标系
plt.plot(angles,data,color='gray',linewidth=2,alpha=0.2)
plt.fill(angles,data,alpha=0.25)
#plt.thetagrids(angles*180/np.pi,radar_labels,frac=1.2)
plt.figtext(0.52,0.95,'霍兰德人格分析',ha='center',size=20)
legend = plt.legend(data_labels,loc=(0.94,0.80),labelspacing=0.2)
plt.setp(legend.get_texts(),fontsize='small')  #legend.get_texts()：获取图例中的所有文本对象,该函数的作用是统一设置图例中文本的字体大小，以便于提高图表的可读性和美观性。
plt.grid(True)
plt.savefig('霍兰德人格分析雷达图.jpg')
plt.show()

