# @Version :1.0
# @Author  :TonyLai
# @File    :py6_4.py
# @Time    :2024/7/13 09:32

g = lambda x: 2*x +1
f = lambda x,y : x + y
print(g(3))
print(f(2,3))

def funX(x):
    return lambda y : x * y
temp = funX(8)
print(temp(4))


temp = filter(None,[1,0,False,True])
print(list(temp))

def odd(x):
    return x % 2
temp = filter(odd,range(20))
print(list(temp))

#lamda
print(list(filter(lambda x: x % 2,range(100))))
# print(list(filter(((lambda x: x % 2)+1), range(0,11))))

temp = list(map(lambda x:x * 2,range(5)))
print(temp)

length =len(range(2**63-1))
print(length)



print(list(reversed(range(10))))
