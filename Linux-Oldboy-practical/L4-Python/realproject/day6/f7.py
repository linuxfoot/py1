#Author: Lzj
#mail: harry_lee2683@outlook.com
from random import sample
import time
print("------李志杰--游戏开发：来自未知星球的敌人----")
a=b=10
j=1
skill={"降龙十八掌":3,"见龙在田":5,"飞龙在天":1,"亢龙有悔":10,"利涉大川":4,"鱼跃于渊":1,"羝羊触潘":3,"损则有孚":1,"屡霜冰至":5}
print("当前战况：你的血值（"+str(a)+") 尼古拉怪兽的血值("+str(b)+")")
c=input("指挥官：是否发动攻击？")
list1=["降龙十八掌","见龙在田","飞龙在天","亢龙有悔","利涉大川","鱼跃于渊","羝羊触潘","损则有孚","屡霜冰至"]
print("-----------")
print("{:s} {:^3s}".format("招式名称"," 伤害值"))
l=m=0
for e in skill:
    l=len(e)-4
    print("{:s}".format(e),end=" ")
    if l>0:
        while m < 2-(2*l-1):
            print(" ",end="")
            m+=1
        print(skill[e])
    else:
        print("{:>4d}".format(skill[e]))
    l=m=0
inp=input('请选择你的第一招：')
k=0
#sel=str(sample(list1,1)).replace('\'',"").replace("[","").replace("]","")
while a >0 and b>0:
    if k == 0 :
        sel=inp
        k=1
    else:
        sel=str(sample(list1,1)[0])
    print("你向怪兽使出了一记："+str(sel)+"（啊。。。。。。。。）,造成伤害"+str(skill[str(sel)])+"点")
    time.sleep(1)
    b=b-int(skill[str(sel)])
    if b<1:
        b=0
        break
    print("当前战况：<你>的血值（"+str(a)+") ,<<尼古拉怪兽>>的血值:("+str(b)+")")
    time.sleep(1)
    print("怪兽开始反击........")
    time.sleep(1)
    sel1=str(sample(list1,1)[0])
    print("<<怪兽>>使出了一记："+str(sel1)+"（我靠！！。。。。不能输！）,造成伤害"+str(skill[str(sel)])+"点")
    time.sleep(1)
    a = a - int(skill[str(sel)])
    if a<1:
        a=0
        break
    print("当前战况：<你>的血值（"+str(a)+")"+" ,<<尼古拉怪兽>>的血值:"+"("+str(b)+")")
    time.sleep(1)
    j+=1
    print("------------第<<<"+str(j)+">>> 回合开始了！-----------")
    time.sleep(2)
if a != 0:
    time.sleep(3)
    print("\n\n")
    print("=========================================")
    print("真正的勇士，你胜利了！！你还剩余"+str(a))
else:
    time.sleep(3)
    print("\n\n")
    print("=========================================")
    print("怪兽的力量不可忽视，请再次应战！怪兽还剩余" + str(b))
print("------李志杰--游戏开发：来自未知星球的敌人----")
print("------李志杰--感谢试玩，感谢一路陪伴----")
exit()
