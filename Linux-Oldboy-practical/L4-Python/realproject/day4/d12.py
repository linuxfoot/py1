#Author: Lzj
#mail: harry_lee2683@outlook.com
i=9
j=1
while i>0:
    while j<=i:
        print("%s * %s =%s" % (i,j,i*j)," ",end="")
        j += 1
    print("\n")
    i-=1
    j=1


