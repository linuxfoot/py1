#Author: Lzj
#mail: harry_lee2683@outlook.com
i=1
j=""
while i<=100:
    j=""
    k=0
    for j in str(i):
        if j == "4":
            k=1
    if k != 1:
        print(i)
    i+=1
