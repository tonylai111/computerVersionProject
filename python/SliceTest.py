# @Version :1.0
# @Author  :TonyLai
# @File    :SliceTest.py
# @Time    :2024/7/8 10:56

# 切片不会改变列表本身的数据机构，新创建了一个拷贝的副本并返回的
list1 = ['钢铁侠','蜘蛛侠','蝙蝠侠','绿灯侠','神奇女侠']
list2 =[list1[1],list1[2],list1[3]]
print(list2)
print(list1[1:4])
print(list1[:])
print(list1[2:])
print(list1[:2])
list1[1:3] = ['超人','闪电侠']
print("切片后对列表赋值",list1)

list3 = range(0,11)
for i in list3:
    print(i)
print(list3)

list4 = [1,2,3,4,5,6,7,8,9]
#指定第三个参数步长 为2
print(list4[1:9:2])
print(list4)
del list4[::2]
print(list4)


