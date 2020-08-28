#Author: Lzj
#mail: harry_lee2683@outlook.com
class father(object):
    var="daddy"
    @classmethod
    def show(self):
        print(self.var)
class son(father):
    pass
class grandson(son):
    pass
class stepfather(object):
    var=1

son1=son()
grandson=grandson()
stepson=stepfather()

sf=stepfather()
print(isinstance(son1,father))
print(isinstance(grandson,father))
print(isinstance(grandson,son))
print(isinstance(stepson,father))
print(isinstance(stepson,son))
print(isinstance(sf,father))
print(isinstance(stepson,stepfather))