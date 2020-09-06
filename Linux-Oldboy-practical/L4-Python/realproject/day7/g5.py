#Author: Lzj
#mail: harry_lee2683@outlook.com
class Chinese:
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')

class Cantonese(Chinese):
    pass # pass表示'跳过'，不执行其他操作

yewen = Cantonese()
print(yewen.eye)
yewen.eat()
