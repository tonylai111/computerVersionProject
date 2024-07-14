# @Version :1.0
# @Author  :TonyLai
# @File    :p4_15.py
# @Time    :2024/7/8 10:21

for year in range(2018,2100):
    if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        break
print("2018年后出现的第一个闰年是：",year)

for year in range(2018,2020):
    if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        break
else:
  print("2018年以后出现的第一个润年是：",year)