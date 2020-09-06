#Author: Lzj
#mail: harry_lee2683@outlook.com
def mon(name,month):
    if month<6:
        res=500
    elif 5<month<13:
        res=120*month
    else:
        res=180*month
    print("亲爱的员工{}: \n 你已经为公司工作了{}个月,获得奖金{}".format(name,month,res))
a=input("name: ")
b=int(input("working month: "))
mon(a,b)
