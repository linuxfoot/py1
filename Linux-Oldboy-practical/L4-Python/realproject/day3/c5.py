#Author: Lzj
#mail: harry_lee2683@outlook.com

class me():
    name="lzj"
    var2="r2"
    @classmethod
    def wo(cls):
        print("my name is:",cls.name)
        print("my var2 is:",str(cls.var2))
me.var2=input('input var2: ')
me.wo()
me.var3=input('input new var3: ')
print(me.var3)
