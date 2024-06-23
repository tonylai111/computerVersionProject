# @Version :1.0
# @Author  :TonyLai
# @File    :Chapter02_7.py
# @Time    :2024/6/23 14:06

import numpy as np
img = np.random.randint(10,99,size=[5,5] ,dtype=np.uint8)
print("img=\n",img)
print("读取像素点img,item(3,2)=",img.item(3,2))
img.itemset((3,2),255)

print("修改后img=\n",img)
