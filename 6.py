#模块与导入:模块就是别人或自己写好的python代码文件，可以重复使用
# #1.1 使用内置模块
# import math
# print(math.sqrt(16)) #4.0
# print(math.pi) #3.141592....

# #1.2  只导入需要的内容：
# from math import sqrt
# print(sqrt(25)) #5.0

#1.3 给模块取简短名字
# import random as rd
# print(rd.randint(1,10)) #随机整数，范围包含1和10
     #假设有两个文件 text.py 和add.py
     # add.py 文件中有
        #def add(a,b):
            # return a+b
    # main.py中
    #from tools import add

        # print(add(3, 5))  # 8