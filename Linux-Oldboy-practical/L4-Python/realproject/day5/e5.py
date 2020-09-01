#Author: Lzj
#mail: harry_lee2683@outlook.com
#遍历二级容器字典
var={("a","b"):[1.1,2.2],("c","d"):[3.1,4.1]}
for i in var:
    x,y=i
    print(x,type(x),y,type(y),var[i])
print(var["a","b"])
