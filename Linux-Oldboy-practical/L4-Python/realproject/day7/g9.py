#Author: Lzj
#mail: harry_lee2683@outlook.com
class Earthman:
    eye_number = 2

# 中国人继承了地球人
class Chinese(Earthman):
    eye_color = 'black'

# 广东人继承了中国人，同时也继承了地球人。
class Cantonese(Chinese):
    pass

yewen = Cantonese()
print(yewen.eye_number)
print(yewen.eye_color)
