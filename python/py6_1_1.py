# @Version :1.0
# @Author  :TonyLai
# @File    :py6_1_1.py
# @Time    :2024/7/13 15:58

def myfunc():
    for i in range(3):
        print("I love fishC")

myfunc()

def div(x,y):
    if y == 0:
        return "除数不能为0"
    return x / y

print(div(4,2))
print(div(4,0))

# def myfun(first,second,third):
#     return "".join((second,first,third))
# print(myfun(first="打了",second="我",third="小甲鱼"))

def myfunc(*args):
    print(f"有{len(args)}个参数")
    print(f"第2个参数是：{args[1]}")

print(myfunc(1,2,3,4,5))

def myfunc(a,*b,**c):
    print(a,b,c)

myfunc(1,2,3,4,5,6,)
help(str.format)


