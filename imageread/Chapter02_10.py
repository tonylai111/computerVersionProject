# @Version :1.0
# @Author  :TonyLai
# @File    :Chapter02_10.py
# @Time    :2024/6/23 14:31

import numpy as np
img = np.random.randint(10,99,size=[2,4,3],dtype=np.uint8)
print("img before\n",img)
img.itemset((1,2,0),255)
img.itemset((0,2,1),255)
img.itemset((1,0,2),255)
print("img after\n",img)