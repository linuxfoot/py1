#Author: Lzj
#mail: harry_lee2683@outlook.com
class snake():
    def __init__(self,var):
        print("========*************---->>")
        print(var)
    def __del__(self):
        print(self ,"is removed")
asnake=snake("ab")
del asnake
