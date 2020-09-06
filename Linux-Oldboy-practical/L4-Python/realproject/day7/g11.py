#Author: Lzj
#mail: harry_lee2683@outlook.com
class C0:
    name='C0'
class C2(C0):
    num=2
class C1:
    num=1
class C3:
    name='C3'
class C4(C1,C2,C3):
    pass

a=C4()
print(C4.num)
print(C4.name)

