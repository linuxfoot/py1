#Author: Lzj
#mail: harry_lee2683@outlook.com
num = [1,2,0,3]
for x in num:
    try:
        print (6/x)
    except ZeroDivisionError:
        print("0 can't be divided")
