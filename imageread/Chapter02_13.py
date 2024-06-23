# @Version :1.0
# @Author  :TonyLai
# @File    :Chapter02_13.py
# @Time    :2024/6/23 14:50

import cv2
import numpy as np
a = cv2.imread("kimi.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("original",a)
face = np.random.randint(0,256,(80,100,3))
a[220:400,250:350] = face
cv2.imshow("result",a)
cv2.waitKey()
cv2.destroyAllWindows()