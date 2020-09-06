# Author: Lzj
# mail: harry_lee2683@outlook.com
from random import choice

def enemy():
    res_enemy = choice(list)

    return res_enemy

def me():
    print(list)
    jud = input("your choice: 1/2/3")
    res_me = list[int(jud) - 1]
    return res_me

def show(a, b):
    print("Enemy: {}, You: {}".format(a, b))

def result(a, b):
    res = ""
    if a != b:

        if a == "bu" and b != "jiandao":
            res = "lose"
        elif a == "jiandao" and b != "shitou":
            res = "lose"
        elif a == "shitou" and b != "bu":
            res = "lose"
        else:
            res = "win"

        print("---------------")
        print("You {}".format(res))
    else:
        print("------SAME---------")

def again():
    global key
    a = input("Continue? y/n")
    if a != "y":
        key = "1"

def main():
    global list
    global key
    key=0
    list = ["shitou", "jiandao", "bu"]
    while key != "1":
        a = enemy()
        b = me()
        show(a, b)
        result(a, b)
        again()
    print("----------END------------")

main()