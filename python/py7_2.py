# @Version :1.0
# @Author  :TonyLai
# @File    :py7_2.py
# @Time    :2024/7/14 10:25

num1 = {1,2,3,4,5}
print(type(num1))
num2 = {}
print(type(num2))

set1 = {1,2,3,4,5}
set1 = set(['python','go','java','javascript'])
print(set1)

print('php' in set1)

set1.add('vue')
set1.remove("go")
print(set1)

# set2 = frozenset({1,2,3,4,5,6})
# set2.add(7)