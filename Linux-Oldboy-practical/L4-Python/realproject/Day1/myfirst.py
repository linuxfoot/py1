print ("Hello,python!")
# comment
'''
this 
is 
for
muilti
comment
'''
a=3
b=4
c,d=10,11
e=f=100
print(a,b)
print(c,d)
print(e,f)
import keyword
print(keyword.kwlist)
李昊阳="fa"
print(李昊阳)
tmp=a
a=b
b=tmp
print(a,b)
b,a=a,b
print(a,b)
res=type(a)
print(res)
res=id(a)
print(res)
intvar=0b100
intvar1=0o117
intvar2=0xff
floatvar=3.14
print(type(intvar))
print(intvar1,type(intvar1))
print(intvar2,type(intvar2))
print(intvar,type(intvar))
print(floatvar,type(floatvar))
floatvar=3.14e2
print(floatvar,type(floatvar))
floatvar=1000e-2
print(floatvar,type(floatvar))
boolvar=True
print(boolvar,type(boolvar))
boolvar=False
print(boolvar,type(boolvar))
complexvar=3+4j
print(complexvar,type(complexvar))
complexvar=4j
print(complexvar,type(complexvar))
res=complex(3,4)
print(res,type(res))
stringvar='ab\nc'
print(stringvar,type(stringvar))
stringvar1="de\nf"
print(stringvar1,type(stringvar1))
stringvar2='''gddddd'd'd
h\niee'e'ee'''
print(stringvar2,type(stringvar2))
stringvar='ab\ncddd\reeee'
print(stringvar,type(stringvar))
stvar='ab"cd"ef'
print(stvar,type(stvar))
stvar="ab\"cd\"ef"
print(stvar,type(stvar))
stringvar3="""'''gddddd'd'd
h\niee'e'ee'''"""
print(stringvar3,type(stringvar3))
stvar=r"ab\t\n"
print(stvar,type(stvar))
strvar="I am%2drole" % (2)
print(strvar,type(strvar))
strvar="I am%-2drole" % (2)
print(strvar,type(strvar))
strvar="I am %f role" % (2.5)
print(strvar,type(strvar))
strvar="I am %.2f role" % (2.5)
print(strvar,type(strvar))
stvar="%s" % ("abcd")
print(stvar,type(stvar))
stvar="我是一个%s,那%d天是%s,我花了%.2f元" % ("fa",1,"sat",3.8888)
print(stvar,type(stvar))
stvar="我是一个%s,那%s天是%s,我花了%s元" % ("fa",1,"sat",3.8888)
print(stvar,type(stvar))