#Author: Lzj
#mail: harry_lee2683@outlook.com
strvar="{} is a {}".format("Harry","faggot")
print(strvar)
strvar="{1} is {0}".format("Harry","Faggot")
print(strvar)
strvar="{name} is {role}".format(name="Harry",role="Faggot")
print(strvar)
strvar="{0[1]} is {1[1]}".format(("Harry","Lily"),["Faggot","Slave"])
print(strvar)
strvar="{g1[0]} is {g2[1]}".format(g1=("Harry","Lily"),g2=["Faggot","Slave"])
print(strvar)
strvar="{g1[0]} is {g2[1]}".format(g1=("Harry","Lily"),g2=["Faggot","Slave"])
print(strvar)
strvar="{g1[0]} is {g2[role2]}".format(g1=("Harry","Lily"),g2={"role1":"Faggot","role2":"Slave"})
print(strvar)
