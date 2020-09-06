#Author: Lzj
#mail: harry_lee2683@outlook.com
class Cat:
    tail = True
    def say(self):
        print('喵喵喵喵喵~')
class C(Cat):
    pass

c1=C()
print(c1.tail)
c1.say()
