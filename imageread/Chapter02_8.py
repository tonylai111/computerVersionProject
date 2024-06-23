# @Version :1.0
# @Author  :TonyLai
# 生成一个灰度图像，让其中的像素值均为随机数。
# @File    :Chapter02_8.py
# @Time    :2024/6/23 14:12

import  numpy as np
import cv2
img = np.random.randint(0,256,size=[256,256],dtype=np.uint8)
cv2.imshow("demo",img)
cv2.waitKey()
cv2.destroyAllWindows()

