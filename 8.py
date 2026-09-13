#1.2继承：继承让子类复用父类已有的属性和方法，并可以增加自己的功能
#
# class 父类名：
#     def __init__(self,参数)
#         self.属性=参数
#     def 父类方法(self):
#         pass
# class 子类名（父类名）：
#     def 子类方法(self):
#         pass


# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print(f"{self.name}:正在吃东西")
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name}:汪汪")
# dog1=Dog("旺财")
# dog1.eat()
# dog1.bark()

# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
#     def start(self):
#         print(f"{self.brand}已经启动")
# class Car(Vehicle):
#     def drive(self):
#         print(f"{self.brand}正在行驶")
# car1=Car("Tesla")
# car1.start()
# car1.drive()

#2.1方法重写：子类可以重新定义父类已有的方法，使它更符合自己的行为。
        #标准格式
# class 父类名:
#     def 方法(self,):
#         print("父类行为")
# calss 子类名(父类名):
#     def 方法名(self):
#     print("子类的新行为")

# class Animal:
#     def make_sound(self):
#         print("动物发出声音")
# class Dog(Animal):
#     def make_sound(self):
#         print("汪汪！")
# class Cat(Animal):
#     def make_sound(self):
#         print("喵喵!")
# dog=Dog()
# cat=Cat()
# dog.make_sound()
# cat.make_sound()


# class Employee:
#     def work(self):
#         print("员工正在工作")
# class Programmer(Employee):
#     def work(self):
#         print("程序员正在编写代码")
# staff1=Employee()
# staff2=Programmer()
# staff1.work()
# staff2.work()

#3.1 子类方法重写后，仍可用super()保留并调用父类原本的功能
    #标准格式
#class 子类名(父类名):
    #def 方法名(self):
        #super().方法名()

# class Employee:
#     def work(self):
#         print("员工正在工作")
# class Programmer(Employee):
#     def work(self):
#         super().work()
#         print("程序员正在编写代码")
# progarmmer=Programmer()
# progarmmer.work()
 
# class Person:
#     def introduce(self):
#         print("我是一个人")
# class Student(Person):
#     def introduce(self):
#         super().introduce()
#         print("我是一名学生")
# student1=Student()
# student1.introduce()


#4.1封装：把对象的数据和操作数据的方法放在一起，并限制外部随意修改重要数据
    #标准格式
# class 类名：
#     def __init__(self,参数):
#         self.属性=参数
#     def 获取数据(self):
#         return self.属性
#     def 修改数据(self,新参数)
#         self.属性=新参数

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     def get_balance(self):
#         return self.balance
#     def deposit(self,amount):
#         if amount > 0:
#             self.balance +=amount
# account=BankAccount("念一",100000000)
# account.deposit(50000)
# print(account.get_balance())

# class Temperature:
#     def __init__(self,number):
#         self.number=number
#     def get_ceksius(self):
#         return self.number
#     def set_celsius(self,data):
#         if data >= -273.15:
#             self.number=data
#         else:
#             print("温度不能低于绝对零度")
# temperature1=Temperature(25)
# temperature1.set_celsius(30)
# print(temperature1.get_ceksius())
# temperature1.set_celsius(-300)
# print(temperature1.get_ceksius())

#5.1 多态：不同类的对象可以使用同一个方法名，但各自执行不同的行为
#     标准格式
# class 类A：
#     def 方法（self):
#         print(A的行为)
# class 类B：
#     def 方法(self):
#         print(B的行为)
# for 对象 in [对象A,对象B]
#     对象.方法名（）

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print(f"园的面积是：{3.14*self.radius**2}")
# class Recatangle:
#     def __init__(self,width,height):
#                 self.width=width
#                 self.height=height

#     def area(self):
#         print(f"长方形的面积是:{self.width*self.height}")
# graphs=[Circle(5),Recatangle(3,4)]
# for graph in graphs:
#     graph.area()

#6.1属性装饰器：可以把一个方法伪装成属性使用。它常用于更安全，自然地读取或修改私有数据
#     标准格式：
# class 类名：
#     @property
#     def 属性名(self):
#         return self._私有属性
#     @属性名.setter
#     def 属性名(self,新参数):
#         self._私有属性=新值

#6.2
# class Person:
#     def __init__(self,age):
#         self.age=age
#     @property
#     def age_get(self):
#         return self.age
#     @age_get.setter
#     def age_get(self,age):
#         if age>= 150:
#             print("年龄不合法")
#         else:
#             self.age=age
# age1=Person(55)

# print(age1.age_get)

# age1.age_get=166
# print(age1.age_get)

#7.2特殊方法__str__:用于定义对象被print()输出时显示的文字，让结果更容易阅读
#格式

# class 类名:
#     def __str__(self):
#         return "要显示的文字"

# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def __str__(self):
#         return f"《{self.title}》-------{self.author}"
# book1=Book("凡人修仙传","忘语")
# print(book1)