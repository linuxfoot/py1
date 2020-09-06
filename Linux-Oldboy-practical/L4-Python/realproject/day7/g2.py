#Author: Lzj
#mail: harry_lee2683@outlook.com
class Chinese:

    def greeting(self):
        print('很高兴遇见你')

    def say(self):
        self.greeting()
        print('我来自中国')

person = Chinese()
# 创建实例person
person.say()
# 调用say()方法
class Chinese:

    def __init__(self):
        print('很高兴遇见你，我是初始化方法')

person = Chinese()

exit()
