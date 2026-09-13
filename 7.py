#面向对象编程(类):用来把数据和功能组织成一个完整对象
#类：对一系列具有相同属性和行为事物的统称，是一个抽象的概念
 #1. 类名 2.属性：对象的特征  3.方法：对象具有的功能
    #基本格式
    #class 类名:                  #先有类，再有对象
    # 代码块，，，
#对象：类的具体表现，面向对象编程的核心
# 基本格式：对象名=类名（）

# class washer:
#     height=10000 #类属性
# print(washer.height) #方法，即对应的功能
 
# class Student:
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age
    # def introduce(self):
    #     print(f"我叫{self.name},今年{self.age}岁。")


# student = Student("念一",19)
# student.introduce()
#1.2 类的属性和方法
# class Dog:
#     def __init__(self,name,age):
#         self.name=name #属性
#         self.age=age #属性
#     def bark(self): #方法
#         print(f"{self.name}:汪汪")
#     def introduce(self):
#         print(f"我叫{self.name},今年{self.age}岁。")
# dog1=Dog("旺财",3)
# dog2=Dog("豆豆",4)
# dog1.bark()
# dog2.introduce()

# class Car:
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
#     def show_info(self):
#         print(f"品牌是{self.brand},已有{self.year}的历史。")
# brand1=Car("特斯拉",20)
# brand1.show_info()

# class Phone:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def show_info(self):
#         print(f"品牌：{self.brand},价格：{self.price}")
# Phone1=Phone("Apple",15999)
# Phone2=Phone("HuaWei",19999)
# Phone1.show_info()
# Phone2.show_info()


class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def show_balance(self):
        print(f"尊敬的{self.owner},你的账户余额是:{self.balance}")
u=BankAccount("念一",1000000000000000)
u.show_balance()

# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         print(f"width*height={self.width*self.height}")
#     def permeter(self):
#         print(f"周长为{2*(self.width+self.height)}")
# rect1=Rectangle(2,3)
# rect1.area()
# rect1.permeter()

class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def is_pass(self):
        return self.score>=60
    def show_result(self):
        if self.is_pass():
            print(f"{self.name}:及格")
        else:
            print(f"{self.name}：不及格")
student1=Student("念一",99)
student1.show_result()

