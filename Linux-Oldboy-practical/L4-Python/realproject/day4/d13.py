#Author: Lzj
#mail: harry_lee2683@outlook.com
i=1
while i<10:
    k=1
    while k<=(63-i*7):
        print(" ",end="")
        k+=1
    j=1
    while j<=i:
        print("%s*%s=%2d" % (i,j,i*j),"" ,end="")
        j += 1
    print()
    i+=1
exit(0)
