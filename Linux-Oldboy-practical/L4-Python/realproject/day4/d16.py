#Author: Lzj
#mail: harry_lee2683@outlook.com
# o 5 x3 c 3 in 1yuan,100
o=5
x=3
i=1
while i<=100:
        j=1
        while j<=100:
            k=1
            while k<=100:
                if (i*o+j*x+k/3 == 100) and (k%3 == 0):
                    if i+j+k == 100:
                        print(i,j,k)
                k+=1
            j+=1
        i+=1

