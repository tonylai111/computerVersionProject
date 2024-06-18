# @Version :1.0
# @Author  :TonyLai
# @File    :Chapter02_2.py
# @Time    :2024/6/18 20:46
imgpath = "/Users/laixiaoming/PycharmProjects/computerVersionProject/resource/liuyifei.jpg"

import cv2
img = cv2.imread(imgpath,0)
cv2.imshow("before", img)
for i in range(10,200):
    for j in range(10,200):
        img[i, j] = 255
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()