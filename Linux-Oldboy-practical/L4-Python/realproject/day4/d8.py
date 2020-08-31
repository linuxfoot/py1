#Author: Lzj
#mail: harry_lee2683@outlook.com
i=100
while i<1000:
    if i%111 ==0:
        print(i)
    a = i // 100
    b = i // 10 % 10
    c = i % (i // 10)
    if (c-b == b-a == 1) or (a-b == b-c == 1):
        print(i,"",end="")
    i+=1
