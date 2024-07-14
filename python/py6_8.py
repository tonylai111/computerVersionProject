# @Version :1.0
# @Author  :TonyLai
# @File    :py6_8.py
# @Time    :2024/7/14 08:52

def fab(n):
    if n < 1:
        return "输入有误！，请重新输入"
    if n == 1 or n == 2:
        return 1
    else:
       return fab(n-1) + fab(n-2)

num = int(input("输入斐波那契数列输入次数："))

result =  fab(num)
print(f"{num}次后,的结果是{result}")