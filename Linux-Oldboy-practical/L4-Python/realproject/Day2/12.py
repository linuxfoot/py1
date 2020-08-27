container=[1,2,3,(10,11,{"a":1,"b":[100,101,"bingo"]})]
res=container[3]
res1=res[2]
res2=res1["b"]
res3=res2[2]
print(res3)
con=container[-1][-1]["b"][-1]
print(con)