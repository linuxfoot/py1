#Author: Lzj
#mail: harry_lee2683@outlook.com
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
    def __str__(self):
        return "Book name is {}, date is {}, status is {}".format(self.name,self.date,self.status)

class manager():

    def registe(self):
        inp=input("book name:")
        dictbd=tod
        dictb=Book(name=inp,date=dictbd)
        dictbook[dictb.name]=dictb
        print(dictbook[dictb.name].date)
        CorE()

    def borrow(self):
        a=input("Input the book name: ")
        res = bm.check(a)
        if res == 0:
            print("Sorry, no book found....!")
        else:

            if dictbook[a].status == "borrowed":
                print("The book {} has already >> {}".format(a,res.status))
            else:
                dictbook[a].status="borrowed"
                dictbook[a].date=tod
                print("----Updated----")
                bm.check(a)
        CorE()

    def returnb(self):
        a = input("Input the book name: ")
        res = bm.check(a)
        if res == 0:
            print("Sorry, no book found....!")
        else:
            if dictbook[a].status == "normal":
                print("The book is not borrowed")
            else:
                dictbook[a].status = "normal"
                dictbook[a].date = tod
                print("----Updated----")
                bm.check(a)
        CorE()

    def search(self):
            a=input("Book name: ")
            res=bm.check(a)
            if res == 0:
                print("Sorry, no book found....!")
            CorE()

    def check(self, a):
        for i in dictbook:
            if i == a:
                print(dictbook[i])
                return dictbook[i]
        return 0

def CorE():
   jud=input("(C)ontinue or (E)xit")
   if jud != "E":
       menu()
   else:
       exi()
def exi():
   print("Thank you. End.")
   exit()

bm = manager()
dictbook = {}
tod=time.strftime("%m%d")
menu()
