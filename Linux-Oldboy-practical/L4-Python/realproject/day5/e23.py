str1="我是一个{a:>>11},{b}的一个{c}".format(a="性感",b="雄性",c="禽兽")
print(str1)
strvar="{name} is {role}".format(name="Harry",role="Faggot")
str2="你有%2d,是一个%s" % (2,"man")
print(str2)
dic={("a","b","e"):[1,2,3],("c","d","f"):[4,5,6,7]}
for i in dic:
    x,y,z=i
    print(x,y,z,dic[x,y,z])