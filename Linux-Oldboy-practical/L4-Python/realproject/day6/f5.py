#Author: Lzj
#mail: harry_lee2683@outlook.com

movie = {'妖猫传':['黄轩','染谷将太'],"甄嬛传":["孙俪","甄嬛"]}
while True:
    a=input('actor name is? ')

    for i in movie:
        if movie[i][0] == a:
            print(a+' is playing role '+movie[i][1]+' in '+i)

exit(0)