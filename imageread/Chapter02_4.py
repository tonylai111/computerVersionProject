# @Version :1.0
# @Author  :TonyLai
# 使用Numpy生成一个三维数组，用来观察三个通道值的变化情况。
# @File    :Chapter02_4.py
# @Time    :2024/6/18 21:27

import numpy as np
import cv2
img = np.zeros((300,300,3), dtype=np.uint8)
img[:,0:100,0] = 255
img[:,100:200,1] = 255
img[:,200:300,2] = 255
print("img\n",img)
# 得到一个蓝绿红相间的颜色图案
cv2.imshow("img=\n",img)
cv2.waitKey()
cv2.destroyAllWindows()