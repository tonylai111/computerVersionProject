# @Version :1.0
# @Author  :TonyLai
# @File    :Chapter02_6.py
# @Time    :2024/6/20 21:27
import cv2
img = cv2.imread("kimi.jpg")
cv2.imshow("before",img)
#区域一
for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            img[i,j,k] = 255 #白色
#区域二
for i in range(50,100):
    for j in range(0,100):
        img[i,j] = [128,128,128] #灰色
#区域三
for i in range(100,150):
    for j in range(0,100):
        img[i,j] = 0 #黑色

cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()