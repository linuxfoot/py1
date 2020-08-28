#Author: Lzj
#mail: harry_lee2683@outlook.com
class me():
    name="lzj"
    var2="r2"
    @classmethod
    def wo(cls):
        print("my name is:",cls.name)
        cls.name=input('new name')
        print("my NEW name is:", cls.name)
        cls.var2=input('new item:')
        print("my new item is:",str(cls.var2))
me.wo()
