# @Version :1.0
# @Author  :TonyLai
# @File    :py6_9.py
# @Time    :2024/7/14 09:17

def hanoi(n,x,y,z):
    if n == 1:
        print(x, '--->',z) #如果只有一层，直接从X移动到Z
    else:
        hanoi(n-1,x,z,y) # 将n-1个盘子，从x移动到y上
        print(x,"--->",z) #将最底下的盘子，从x移到z上
        hanoi(n-1,y,x,z) #将y上的63个盘子移到z上
n = int(input("请输入汉诺塔的层数："))
hanoi(n,'X','Y','Z')