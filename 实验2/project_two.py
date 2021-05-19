import matplotlib.pyplot as plt #添加头文件
import numpy as np
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)#创建x轴数据
y = np.sin(x)    #创建y轴数据

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)  #一行两列第一个图
plt.title(r'$f(x)=sin(x)$')#给第一幅图加标题
plt.plot(x, y)#绘制第一个波形
#plt.show()

x1 = [t*0.375*np.pi for t in x]#创建x轴的数据
y1 = np.sin(x1)#创建y轴数据
plt.subplot(1,2,2)#一行两列第二个图
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$')#加上第二幅图的标题
plt.plot(x1, y1) #绘制第二个波形
plt.show()#将波形输出