#Author: Lzj
#mail: harry_lee2683@outlook.com
from random import choice
def menu(*barbeque):
    return barbeque

order = menu('烤鸡翅','烤茄子','烤玉米')
#括号里的这几个值都会传递给参数barbeque

print(order)
print(type(order))
def menu(*barbeque):
    for i in barbeque:
        print('一份烤串：' + i)
menu('烤香肠', '烤肉丸')
menu('烤鸡翅', '烤茄子', '烤玉米')
print('金枪鱼', '三文鱼', '鲷鱼')
print('金枪鱼', '三文鱼', '鲷鱼', sep = '+')
# sep控制多个值之间的分隔符，默认是空格
print('金枪鱼', '三文鱼', '鲷鱼', sep = '+', end = '=?')

gifts=["apple phone","apple watch","apple tv"]
def cou(a):
    if a>10:
        res=choice(gifts)+'+BMW bike'
    else:
        res=choice(gifts)
    return res
print()
print(cou(5))
print(type(cou(11)))