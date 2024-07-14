# @Version :1.0
# @Author  :TonyLai
# @File    :SinglePreceptron.py
# @Time    :2024/7/6 10:26

import numpy as np
import matplotlib.pyplot as plt

#定义输入，习惯上用一行表示一个数据
X = np.array([[1,3,3],[1,4,3],[1,1,1],[1,2,1]])
#定义标签，习惯上用一行表示一个数据标签
T = np.array([[1],[1],[-1],[-1]])
#权值初始化，3行1列
W = np.random.random([3,1])
#学习率设置0.1
lr = 0.1
#神经网络的输出
Y = 0
#更新一次权值train()方法
def train():
    global W
#训练100次
    #数据的预测值Y，形状为4行1列
    Y = np.sign(np.dot(X,W))
    E = T - Y
    delta_W = lr*(X.T.dot(E))/X.shape[0]
    W = W + delta_W

#训练100次
for i in range(100):
    train()
    print("epoch:",i+1)
    print("weighs",W)
    Y = np.sign(np.dot(X,W))
    if(Y == T).all():
        print("Finished!")
        break
"""
画图
"""
#正样本x,y坐标
x1 = [3,4]
y1 = [3,3]
#负样本x,y坐标
x2 = [1,2]
y2 = [1,1]

k = -W[1]/W[2]
d = -W[0]/W[2]
xdata = (0,5)

plt.plot(xdata,xdata*k+d,'r')
#蓝色的点画出正样本
plt.scatter(x1,y1,c='b')
#黄色的点画出负样本
plt.scatter(x2,y2,c='y')
plt.show()