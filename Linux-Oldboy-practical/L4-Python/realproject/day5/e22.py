str="There are moments in life when you miss someone so much that you just want to pick them from your dreams and hug them for real! Dream what you want to dream;go where you want to go;be what you want to be,because you have only one life and one chance to do all the things you want to do"
res=str.find("o")
j=0
while j != -1:
    j=str.find("o",res)
    print(j)
    res = j+1