# @Version :1.0
# @Author  :TonyLai
# @File    :py5_3_2.py
# @Time    :2024/7/10 06:59

first = "{0} love {1} {2}".format('tony','python','very much')
print(first)

second = "{a} love {b} {c}".format(a='tony',b='python',c='very much')
print(second)

third = "{0} love {a} {b}".format('tony',a = 'english',b = 'very much')
print(third)

fouth = "{a} love {b} {d}".format(a ='tony',b = 'python',d ='very much')
print(fouth)

five = "{{0}}".format("不打印0")
print(five)

six = "{0}:{1:.2f}".format("圆周率",3.14159)
print(six)

seven = "{0:}{1:.3f}".format("e =",2.141516)
print(seven)

a = '%c' % (97 + 25)
print(a)

b = '%f 用科学计数法表示为：%e' %(14950000,14950000)
print(b)

c = '%d转化为八进制是：%x' %(123,123)
print(c)

str1 = "hello "
str2 = "mortor"
d = "%s%s" % (str1,str2)
print(d)
name = 'zhangsan'
score = 100
e = 'result is %s:%d' %(name,score)
print(e)

print('\a')