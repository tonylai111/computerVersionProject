# @Version :1.0
# @Author  :TonyLai
# @File    :py5_1.py
# @Time    :2024/7/8 10:31

number = [1,2,3,4,5]
#append 向列表中添加元素
number.append(6)
#extend() 向列表中扩展一个列表
number.extend([7,8])
#insert指定某个元素插入某个值
number.insert(0,0)
#可以倒数来插入数据
number.insert(-1,9.9)
print(number)

eggs = ['鸡蛋','鸭蛋','鹅蛋','铁蛋']
print(eggs[0])
print(eggs[(len(eggs) - 1)])

#位置调换，采用temp
# temp = eggs[1]
# eggs[1] = eggs[3]
# eggs[3] = temp
# print(eggs)
# 位置调换方法
eggs[0],eggs[3] = eggs[3],eggs[0]
print(eggs)

import random
prizes =  ['鸡蛋','鸭蛋','鹅蛋','铁蛋']
#random.choice 随机获取一个元素
answer = random.choice(prizes)
print(answer)

## 列表的删除有三种方法 pop ,remove ,del

eggs.pop(1)
print(eggs)
eggs.remove('铁蛋')
print(eggs)
del eggs[1]
print(eggs)