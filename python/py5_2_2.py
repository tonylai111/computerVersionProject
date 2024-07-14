# @Version :1.0
# @Author  :TonyLai
# @File    :py5_2_2.py
# @Time    :2024/7/8 15:39

x_men = ('金刚狼','x教授','暴风女','火凤凰','镭射眼')
# x_men[1] = '雄霸天下'
x_men = (x_men[0],'雄霸天下')+ x_men[2:]
print(x_men)

x_men = x_men[:1] + x_men[2:]
print(x_men)