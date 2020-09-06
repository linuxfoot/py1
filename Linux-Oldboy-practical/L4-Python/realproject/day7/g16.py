#Author: Lzj
#mail: harry_lee2683@outlook.com
import time
def menu():
    print('''
    ------------Book Manager System--------------
    1. registe book
    2. borrow book
    3. return book
    4. search book
    5. quit
    ''')
    jud = input("your number:")


    if jud == "1":
        bm.registe()

    if jud == "2":
        bm.borrow()

    if jud == "3":
        bm.returnb()

    if jud == "4":
        bm.search()

    if jud == "5":
        exi()


class Book():
    def __init__(self,name,status="normal",date="0000"):
        self.name=name
        self.status=status
        self.date=date

class manager():

    def registe(self):
        inp=input("book name:")
        dictbd=tod
        global dictb
        dictb=Book(name=inp,date=dictbd)
        dictbook[dictb.name]=[dictb.name,"normal",dictb.date]
        CorE()

    def borrow(self):
        bm.searchin(status="normal")
        jud=input("Input the book name: ")
        dictbook[jud][1]="borrowed"
        dictbook[jud][2]=tod
        bm.searchin(status="borrowed")
        CorE()

    def returnb(self):
        bm.searchin(status="borrowed")
        jud = input("Input the book name: ")
        dictbook[jud][1] = "normal"
        dictbook[jud][2] = tod
        bm.searchin(status="normal")
        CorE()

    def search(self):
        jud=input("Search (N)ame or (S)tatus:")
        if jud == "N":
            a=input("Book name: ")
            res=bm.searchin(name=a)
            if  res :
                print(res)
            else:
                print("Sorry, no result found...")
        else:
            b=input("Status:(normal/borrowed)")
            res=bm.searchin(status=b)
            if res :
                print(res)
            else:
                print("Sorry, no result found...")
        CorE()
    # in

    def searchin(self,name="xxx",status="xxx",date="xxx"):
        self.name=name
        self.status=status
        self.date=date
        for i in dictbook:
            if dictbook[i][0] == self.name or dictbook[i][1] == self.status or dictbook[i][2] == self.date:
                a,b,c=dictbook[i]
                print(a,b,c)
def CorE():
   jud=input("(C)ontinue or (E)xit")
   if jud != "E":
       menu()
   else:
       exi()
def exi():
   print("Thank you. End.")
   exit()

global dictbook
bm = manager()
dictbook = {}
tod=time.strftime("%m%d")
menu()


