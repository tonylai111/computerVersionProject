# @Version :1.0
# @Author  :TonyLai
# @File    :py6_5_2.py
# @Time    :2024/7/14 08:31


# def recursion(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
#
# number = int(input("请输入一个整数："))
# result = recursion(number)
# print(result)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("请输入一个整数："))
result = factorial(num)
print("%d的阶乘递归的结果是%d"%(num,result))
