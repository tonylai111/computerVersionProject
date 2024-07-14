# @Version :1.0
# @Author  :TonyLai
# @File    :py5_3_1.py
# @Time    :2024/7/8 20:48

str1 = 'FishC'
#所有字母变成小写
case = str1.casefold()
print(case)

str2 = "上海自来水来自海上"
count1 = str2.count('上')
print(count1)

print(str2.count('自',0,len(str1)-1))

str3 = 'i love you'
var = str3.replace('you','fishc.com')
print(var)

str5 = "肖申克的救赎/1991年/9.6分/美国"
var2 = str5.split(sep='/')
print(var2)

idx_find = str5.find('张')
# idx_index = str5.index('张')
print(f'idx',idx_find)
# print(idx_index)

countries = ['中国','俄罗斯','美国','日本','英国','法国']

str = '-'.join(countries)
str2 = ''.join(countries)
list1 = str.split('-')
print(str)
print(list1)
print(str2)
list2 = str2.split()
print(list2)