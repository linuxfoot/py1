class pri(object):
    def __init__(self):
        self._acount = 1
        self.__acountt = 2
        self.a="aaaaaaaaaa"
    def __len__(self):
        return len(self.a)
    def showt(self):
        return self._acount
    def showtt(self):
        return self.__acountt
    def showa(self):
        return self.a

person=pri()
print(dir(person))
print(person.__dict__)
print(person.showt())
print(person.showtt())
print(person._pri__acountt)
print(person.showa())
print(person.__len__())

