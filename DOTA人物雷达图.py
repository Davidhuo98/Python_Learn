import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
labels = np.array(['综合','KDA','发育','推进','生存','输出'])
nAttr = 6
data = np.array([7,5,6,9,8,7])
angles = np.linspace(0,2*np.pi,nAttr,endpoint=False) # `endpoint=False`: 这个参数指明了生成的线性空间是否包含终止点。当`endpoint=False`时，生成的线性空间将不包含终止点`2*np.pi`
data = np.concatenate((data,[data[0]]))
angles = np.concatenate((angles,[angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111,polar=True) # polar=True参数表示这个子图是极坐标系
plt.plot(angles,data,color='g',linewidth=2)
plt.fill(angles,data,facecolor='g',alpha=0.25)
#plt.thetagrids(np.array([angles[0]])*180/np.array([np.pi]), labels)
plt.figtext(0.52,0.95,'DOTA能力值雷达图',ha='center')
plt.grid(True)  #该函数用于在图表中显示或隐藏网格线。调用plt.grid(True)时，会在图表中显示网格线，其中True表示启用网格线，也可以设置为False来禁用网格线
plt.savefig('dota_radar,jpg')
plt.show()


