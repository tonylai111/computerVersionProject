# @Version :1.0
# @Author  :TonyLai
# @File    :NumpyStudy01_7_1.py
# @Time    :2024/6/21 06:17

a = [1,2,3,4,5]
b = [2,3,4,5,6]

for i in range(5):
    a[i] = a[i] + 1
print(a)

import numpy as np
a  = np.array([1,2,3,4,5,6])
# b  = np.array([1,2,3,4,5,6])
# c = a + b
# numpy 有广播机制，1维数组和2维数组相加，a会自动扩展一维，然后每个位置的元素分别相加
d = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
e = a + d
print(e)

########
# 创建ndarray数组的几种方式
########
#从list创建array
a = [1,2,3,4,5,6]
b = np.array(a)
print(b)

#通过np.arrange创建 start,stop(不包含本身) ,interval步长3
a = np.arange(0,10,3)
print(a)

#zeros创建全为0或者形状全为0的数组
a = np.zeros([4,5])
print(a)

#ones创建全为1的数组
a = np.ones([8,8])
print(a)

########
# 查看ndarray数组的属性
########
# ndarray属性有 shape,dtype,size ,ndim
# shape 数组的形状
# dtype 数组数据类型
# size 元素个数
# ndim 数组维度大小，等于shape的个数
a = np.ones([3,3])
print(f"a的属性dtype:{a.dtype},\nshape:{a.shape},\nsize:{a.size},\nndim:{a.ndim}")

a = np.random.rand(10,10,10,10)
print(f"a的属性dtype:{a.dtype},\n shape:{a.shape},\nsize:{a.size},\nndim:{a.ndim}")

########
# 改变ndarray数组的数据类型和形状
########
#转换数据类型
a = a.astype(np.int16)
print(a.dtype)
#改变形状
a = a.reshape(100,100)
print(f"type:{a.dtype},shape:{a.shape}")

########
# 数组的基本运算
########

arr = np.array([[1,2,3],[4,5,6]])
print(1/arr)

