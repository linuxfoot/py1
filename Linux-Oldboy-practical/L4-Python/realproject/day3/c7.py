#Author: Lzj
#mail: harry_lee2683@outlook.com
class dll():
    name="dll"
    age="28"
    @classmethod
    def fir(cls):
        print("my name is: "+cls.name)
dll.fir()
lzj=dll()
print("lzj.name is; ",lzj.name)
dll.name="DLL"
print("lzj.name is; ",lzj.name)
def new(self):
    print("new fun!!")
lzj.fir()
def newlzj():
    print("new lzj fun!!")
lzj.fir=newlzj
lzj.fir()
dll.fir()
