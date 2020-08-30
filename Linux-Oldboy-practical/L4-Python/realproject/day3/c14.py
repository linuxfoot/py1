class userr(object):
    def __init__(self,name):
        self.nam=name
    @classmethod
    def hello(cls):
        print("Welcome user: ",cls.nam)

class genuser(userr):
    def hello(self):
        print("you are",self.nam,"welcome")

class vipuser(userr):
    def hello(self):
        print("welcome VIP!!!",self.nam)

def runner(userhi):
    userhi.hello()

lzj=genuser("lzj")
lhy=vipuser("lhy")

runner(lzj)
runner(lhy)


