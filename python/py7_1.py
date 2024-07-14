# @Version :1.0
# @Author  :TonyLai
# @File    :py7_1.py
# @Time    :2024/7/14 09:49

a = dict(one = 1,two =2 ,three =3)
b = {'one':1,"two":2,"three":3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict({"one":1,"two":2,"three":3})
print(type(a))
print(b)
print(c)
print(d)
print(a == b == c == d)