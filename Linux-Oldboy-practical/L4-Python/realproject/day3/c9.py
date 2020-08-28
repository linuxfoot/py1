#Author: Lzj
#mail: harry_lee2683@outlook.com
class father(object):
    var="daddy"
    @classmethod
    def show(self):
        print(self.var)
f1=father()
f1.show()

class son(father):
    pass
    sonvar="l"
    @classmethod
    def show(self):
        print(self.var)

son.var="I am son."
son.show()
print(dir(son))
print(son.__dict__)
print(get_)
