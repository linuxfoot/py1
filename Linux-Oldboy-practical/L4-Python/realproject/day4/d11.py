#Author: Lzj
#mail: harry_lee2683@outlook.com
i=1
j=1
while i<=10:
    while j<=i:
        print(i,"*",j,"=",i*j,"  ",end="")
        j+=1
    if j == 10:
        print("\n")
    i+=1
    j=1
