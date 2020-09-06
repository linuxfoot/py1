#Author: Lzj
#mail: harry_lee2683@outlook.com
# 工时计算公式
import math
size = 1.5
number = 2
time = size * 80 / number

# 人力计算公式
size = 0.5
time = 20.0
number = size * 80 / time

def main1(a,b):
    time=a*80/b
    print("需要{}个工时".format(time))

def main2(a,b):
    num = math.ceil(a * 80 / b)
    print("需要{}个人".format(num))

jud=input("请选择：1 工时计算 2 人力计算")
if jud == '1':
    a=float(input("size: "))
    b=int(input("num: "))
    main1(a,b)
else:
    a = float(input("size: "))
    b = int(input("time: "))
    main2(a, b)