#Author: Lzj
#mail: harry_lee2683@outlook.com
#
var={10:1,20:2}
for i in var.values():
    print(i)
while i <100:
    if i//10%2 == 0:
        print("@",end="")
    else:
        print("%",end="")
    if i % 10 == 9:
        print()
    i += 1


