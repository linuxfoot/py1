#Author: Lzj
#mail: harry_lee2683@outlook.com
i=100
while i<1000:
    res=str(i)
    if (int(res[0])+1 == int(res[1])):
        if (int(res[1])+1 == int(res[2])):
            print(i)
    if (int(res[0]) - 1 == int(res[1])):
        if (int(res[1]) - 1 == int(res[2])):
            print(i)
    if i % 111 == 0:
        print(i)
    i+=1

