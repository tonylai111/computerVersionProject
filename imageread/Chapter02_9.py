# @Version :1.0
# @Author  :TonyLai
# @File    :Chapter02_9.py
# @Time    :2024/6/23 14:23
import cv2
img = cv2.imread("kimi.jpg",0)
print("读取像素点img,img.item(3,2)",img.item(3,2))
img.itemset((3,2),255)
print("修改后像素点img.item(3,2) = ",img.item(3,2))

# 测试修改的一个区域的像素值
cv2.imshow("before",img)
for i in range(10,100):
    for j in range(80,100):
        img.itemset((i,j),255)
cv2.imshow("after",img)

cv2.waitKey()
cv2.destroyAllWindows()
