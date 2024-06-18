# @Version :1.0
# @Author  :TonyLai
# @File    :Chapter02.py
# 使用Numpy库中的函数zeros()可以生成一个元素值都是0的数组，
# 并可以直接使用数组的索引对其进行访问、修改。
# @Time    :2024/6/18 20:28

import cv2
import numpy as np
#生成8行8列的二维全是0的数组
img = np.zeros((8,8),dtype=np.uint8)
print("img = \n", img)
cv2.imshow("one", img)
print("读取像素点img[0,3]", img)
#修改像素点 ,注意这里是从0开始
img[0,3] = 255
img[7,7] = 125
print("修改后像素点img[0,3]= \n", img[0,3])
cv2.imshow("two",img)
print("update img\n",img)


cv2.waitKey()
cv2.destroyAllWindows()