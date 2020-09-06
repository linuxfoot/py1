#Author: Lzj
#mail: harry_lee2683@outlook.com
class robot():
    def __init__(self,name,myname):
        self.name=name
        self.myname=myname
        self.sayhi()

    def sayhi(self):
        print("hello {}, I am a robot , my name is {}".format(self.myname,self.name))

    def saywish(self,a):
        i=0
        for i in range(0,3):
            print("Your wish is {} ".format(a))
            i+=1

name=input("You want robot's name is :")
myname=input("Your name is :")
wish=input("Your wish is: ")
ro=robot(name,myname)
ro.saywish(wish)
exit()
