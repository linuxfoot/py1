strvar="i am a good boy ABC &abc $log #efg AAA"
res=strvar.count("a",0,6)
res=strvar.index("a",3)
res=strvar.startswith("A",16)
res=strvar.endswith("A",-5,-2)
res=strvar.split()
print(res)
res="-".join(res)
print(res)
res=res.replace("-","@")
print(res)