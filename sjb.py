'''
这是一个石头剪刀布游戏
主要是为了熟悉下PY的if else写法和随机函数的使用
'''
import random

'定义一个随机数RAN'
a = "0"
b = "1"
c = "2"
pc = random.randint(0, 2)
'石头a，剪刀b，布c'

hm = input("请输入！【0】代表石头、【1】代表剪刀、【2】代表布 \n")
"输出玩家的结果"
if hm == str(0):
    print("玩家出的是石头！")
elif hm == str(1):
    print("玩家出的是剪刀！")
elif hm == str(2):
    print("玩家出的是布！")
print("----------VS----------")
"输出PC的结果"
if pc == 0:
    print("电脑出的是石头！\n")
elif pc == 1:
    print("电脑出的是剪刀！\n")
elif pc == 2:
    print("电脑出的是布！\n")
print("结果是：")
"给出判断规则"
"玩家能赢的结果只有："
if (int(pc) == 1 and int(hm) == 0) or (int(pc) == 2 and int(hm) == 1) or (int(pc) == 0 and int(hm) == 2):
    print("本局为玩家胜利！")
elif int(pc) == int(hm):
    print("本局为平局！")
else:
    print("本局为电脑胜利！")
