'''
listvar=["abc","def",8.9,True,4+3j]
print(listvar,type(listvar))
res=listvar[-1]
print(res)
res=listvar[2]
print(res)
num=len(listvar)
print(num)
res=listvar[num-1]
print(res)
res=listvar[5-1]
print(res)
print(listvar[len(listvar)-1])
listvar[0]="begin"
res=listvar[0]
print(res)
print(listvar)
tuplevar=("a","b","c")
print(tuplevar,type(tuplevar))
res=tuplevar[-3]
print(res)
res=tuplevar[2]
print(res)

#tuplevar[2]="abc"
'''
tuplevar1=(123)
print(tuplevar1,type(tuplevar1))
tuplevar1=(123,)
print(tuplevar1,type(tuplevar1))
tuplevar1=1,2,3
print(tuplevar1,type(tuplevar1),"a")
strvar="abcd efg"
res=strvar[3]
print(res)

strvar="abc\nd efg"
res=strvar[4]
print(res,"<>")
res=strvar[5]
print(res,"<>")
res=strvar[3]
print(res,"<n>")

