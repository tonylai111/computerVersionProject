# @Version :1.0
# @Author  :TonyLai
# @File    :py6_3_1.py
# @Time    :2024/7/13 08:48

def log(func):
    def wrapper(name):
        print("开始调用eat()函数。。。")
        func(name)
        print("结束调用eat()函数")
    return wrapper

def log2(func):
    def warpper(*params):
        print("开始调用eat()函数。。。")
        func(*params)
        print("调用eat函数结束。。。")
    return warpper

# @log
@log2
def eat(name,count,weight):
    print(f"{name}开始吃了,吃了{count}条鱼 ")
    print("%s开始吃了，吃了%d条鱼，这条鱼有%.1f斤"%(name,count,weight))


eat("小甲鱼",100,3.003)