#Author: Lzj
#mail: harry_lee2683@outlook.com
strvar="你是一个什么样的?"
res=strvar[5:]
print(res)
res=strvar[:5]
print(res)
res=strvar[2:4]
print(res)
res=strvar[::2]
print("tag",res)
res=strvar[::-1]
print(res)
res=strvar[:]
print(res)
res=strvar[::]
print(res)

res=strvar[-5:-1]
print(res)
res=strvar[-2:-6:-1]
print(res)
#你是一个什么样的?