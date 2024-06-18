# @Version :1.0
# @Author  :TonyLai
# @File    :Chapter02_3.py
# 使用Numpy生成三维数组，用来观察三个通道值的变化情况。
# @Time    :2024/6/18 21:12
import numpy as np
import cv2
#蓝色通道
blue = np.zeros((300,300,3),dtype=np.uint8)
# 对数组blue,将其第0个通道设置为255，其他的为0，因此为蓝色
blue[:,:,0] = 255
print("blue=\n", blue)
cv2.imshow("blue", blue)

#绿色通道
green = np.zeros((300,500,3),dtype=np.uint8)
# 对数组green，将其第一个通道设置为256，其他的为0，因此为绿色
green[:,:,1] = 255
print("green=\n",green)
cv2.imshow("green",green)

#红色通道
red = np.zeros((256,256,3),dtype=np.uint8)
#针对数组red,将其第二个通道设置为255，其他的为0，因此为红色
red[:,:,2] = 255
print("red\n",red)
cv2.imshow("red",red)

cv2.waitKey()
cv2.destroyAllWindows()