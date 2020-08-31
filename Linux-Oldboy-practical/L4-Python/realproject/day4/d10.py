#Author: Lzj
#mail: harry_lee2683@outlook.com
'''
i=1
j=1
while i<=10:
    print("*",end="")
    i+=1
str="I"
str1=" am"
str2=" a boy"
res=str+str1+str2
print(res)
str3=""
while j<=10:
    str3 += "*"
    j+=1
print(str3)

i=1
j=2
while i<=10:
    if i%2 == 0:
        print("黑",end="")
    else:
        print("白", end="")
    i+=1

i=1
j=1
while i<=10:
    while j<=10:
        if j<10:
            print("*",end="")
        else:
            print("*")
        j+=1
    j=1
    i+=1

i=1
j=1
while i<=10:
    while j<=10:
        if j%2 ==0:
            a="*"
        else:
            a="-"
        if j<10:
            print(a,end="")
        else:
            print(a)
        j+=1
    j=1
    i+=1
i=1
j=1
while i<=10:
    if i%2 ==0:
        a="*"
    else:
        a="-"
    while j<=10:

        if j<10:
            print(a,end="")
        else:
            print(a)
        j+=1
    j=1
    i+=1

i=1
j=1
strv=""
while i<=10:
    if i%2 ==0:
        a="*"
    else:
        a="-"
    while j<=10:
        strv += a
        j+=1
    print(strv)
    strv=""
    j=1
    i+=1
i=1
while i<=100:
    if i%10 != 0:
     print("*",end="")
    else:
     print("\n",end="")
    i+=1
i=1
a=""
while i<=100:
    if i%2 ==0:
        a="*"
    else:
        a="-"
    if i%10 != 0:
     print(a,end="")
    else:
     print("\n",end="")
    i+=1
i=1
a="*"
while i<=100:

    if i%10 != 0:
     print(a,end="")

    else:
     print("\n",end="")
     if a == "*":
      a="-"
     else:
      a="*"
    i+=1
'''
i=1
j=0
a=""
while i<=100:
    if j%2 ==1:
        if i % 2 == 0:
            a = "★"
        else:
            a = "☆"
    else:
        if i % 2 == 0:
            a = "☆"
        else:
            a = "★"
    if i%10 != 0:
     print(a,end="")
     j
    else:
     print("\n",end="")
     j+=1
    i+=1

