# @Version :1.0
# @Author  :TonyLai
# @File    :py7_1_2.py
# @Time    :2024/7/14 09:59

dict1 = {}
result =  dict1.fromkeys((1,2,3))
print(result)

dict2 = {}
result = dict2.fromkeys((1,2,3),('a','b','c'))
print(result)


dict3 = {}
dict3 = dict3.fromkeys(range(10),"赞")
print(dict3.keys())
print(dict3.values())
print(dict3.items())

print(dict3.get(30,'没有呀'))

print(2 in dict3)
print(20 in dict3)

a  = {1:'one',2:'two',3:'three'}
b = a.copy()
a[2] = 'xiaobai'
print(a)
print(b)

a.setdefault(4)
print(a)

pets = {"米奇":"mouse","汤姆":"cat","犇犇":'cow'}
pets.update(哈士奇 = "dog")
print(pets)

