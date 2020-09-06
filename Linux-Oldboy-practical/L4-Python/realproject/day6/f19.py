#Author: Lzj
#mail: harry_lee2683@outlook.com
deposit = [100,300,900,2000,5000,0,2000,4500]
for i in range(1, len(deposit)):
    try:
        times = deposit[i]/deposit[i-1]
    except ZeroDivisionError:
        print("error")
    print('你的存款涨了%f倍'%times)
