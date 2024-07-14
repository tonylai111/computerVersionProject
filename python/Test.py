# @Version :1.0
# @Author  :TonyLai
# @File    :Test.py
# @Time    :2024/7/8 09:03
#
# print((not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8) or (8 and 9))
#
# print(5 and 6)
# for each in 'FinshC':
#     print(each)

for year in range(2018,2050):
    if(year % 4 == 0) and (year % 100 != 0) or(year % 400 == 0):
        print(year)
        continue

# while 条件
# 循环体
# else
# 条件不成立是执行的内容

# for 变量 in 可迭代对象
# 循环体
# else
# 条件不成立是执行的内容

sum  = 0
for i in range(101):
    sum += i
print(sum)

sum2 = 0
for i in range(101):
    sum2 += i
else:
    print(sum2)