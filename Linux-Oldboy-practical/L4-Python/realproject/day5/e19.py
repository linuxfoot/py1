#Author: Lzj
#mail: harry_lee2683@outlook.com
s=int(input("Input your number: "))
i=1
while i<=s:
    j=str(i)
    k=0
    if j[-1] == "4":
        i+=1
        continue
    else:
        while k < len(j):
            if k == "4":
                break
            else:
                k+=1
        print(j)
    i+=1
exit(0)