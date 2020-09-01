#Author: Lzj
#mail: harry_lee2683@outlook.com
#用变量解包方式，遍历等长二级容器
var=([1,2],["a","b"])
for i in var:
    a,b=i
    print(a,",",b)
