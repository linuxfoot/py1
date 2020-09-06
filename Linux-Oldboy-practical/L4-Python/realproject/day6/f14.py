#Author: Lzj
#mail: harry_lee2683@outlook.com
import time
from random import choice
img='''     _ooOoo_
 4                   o8888888o
 5                   88" . "88
 6                   (| -_- |)
 7                   O\  =  /O
 8                ____/`---'\____
 9              .'  \\|     |//  `.
10             /  \\|||  :  |||//  
11            /  _||||| -:- |||||-  
12            |   | \\\  -  /// |   |
13            | \_|  ''\---/''  |   |
14            \  .-\__  `-`  ___/-. /
15          ___`. .'  /--.--\  `. . __
16       ."" '<  `.___\_<|>_/___.'  >'"".
17      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
18      \  \ `-.   \_ __\ /__ _/   .-` /  /
19 ======`-.____`-.___\_____/___.-`____.-'======
20                    `=---='
'''
def luck(a,b,c):
    lucklist=[a,b,c]
    person=choice(lucklist)
    print(img)
    print("Our final lucky person is {}".format(person))

luck("李志杰","李昊阳","张天宇")
