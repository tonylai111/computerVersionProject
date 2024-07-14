# @Version :1.0
# @Author  :TonyLai
# @File    :py5_1_7.py
# @Time    :2024/7/8 11:24

old_list = ['西班牙','葡萄牙','葡萄牙','牙买加','匈牙利','奥地利','孟买']
new_list =[]

for area in old_list:
    if area not in new_list:
        new_list.append(area)
print(new_list)
print(dir(list))

#统计某个元素在列表中出现的次数
count = old_list.count('葡萄牙')
print(count)
#列表中第一次出现的索引值
idx = old_list.index('牙买加')
print(idx)

# 将列表反转
old_list.reverse()
# print(old_list)
# list2 = ['a','c','b','f','e']
# list3 = [1,32,3,5,2,6]
list4 = [8,9,3,5,2,6,10,1,0]
# print(list2)
# print(f"reverse:{list2.reverse()}",list2.reverse())
# print(f'sort:{list2.sort(reverse=True)}',list2.sort(reverse=True))
# print(f'list3:{list3.reverse()}',list3.reverse())
print('old list',old_list.reverse())