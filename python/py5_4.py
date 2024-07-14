# @Version :1.0
# @Author  :TonyLai
# @File    :py5_4.py
# @Time    :2024/7/10 21:09

a  = list()
print(a)
b = list('hello world')
print(b)

c = list((1,2,3,4,5,6,7))
print(c)

d = tuple('list')
print(d)

f = str(123)
print(type(f))

g = 'i love tony panda'
print(len(g))

list1 = [1,2,3,4,5]
print(len(list1))

tuple1 = "这",'是','一个','元组'
print(len(tuple1))

list2 = [1,18,13,0,-89,34,54,75,32]
h = max(list2)
i = min(list2)
print(h)
print(i)

j = sum(list2)
print(j)

list1 = [-98,0,1,13,18,32,34,54,76]
list2 = list1[:]
print(sorted(list1))
print(list2)

for each in reversed(list1):
    print(each)
