# @Version :1.0
# @Author  :TonyLai
# @File    :NumpyStudy.py
# @Time    :2024/6/21 06:03

import numpy as np
import matplotlib.pyplot as plt

# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])
# c = a + b

# d = np.linspace(0,2*np.pi,50)
# print(d)
# e = np.sin(d)
# print(e)
#
# mask = d >= 0
# plt.plot(d[mask],e[mask],'bo')
# mask = (e >= 0)&(d <= np.pi/2)
# plt.plot(d[mask],e[mask],'go')
# plt.show()

a = np.linspace(0,2*np.pi,50)
print(a)
b = np.sin(a)
print(b)
mask = b >= 0
plt.plot(a[mask],b[mask],'bo')
mask = (b >= 0)&(a<=np.pi/2)
plt.plot(a[mask],b[mask],'go')
plt.show()