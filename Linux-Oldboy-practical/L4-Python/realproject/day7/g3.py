#Author: Lzj
#mail: harry_lee2683@outlook.com
class Chinese:
    def __init__(self,town):
        self.hometown=town

    def born(self):
        print('我出生在%s。' % self.hometown)


wufeng = Chinese('广东')
wufeng.born()
