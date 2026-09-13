#类属性和实例属性
#1.1类属性：所有对象共享的数据
#1.2实例属性：每个对象各自拥有的属性
        #标准格式
# class 类名:
#     类属性=值
#     def __init__(self,参数):
#         self.实例属性=参数

#1.3例子：
# class Student:
#     school="龙南中学" #类属性
#     def __init__(self,name):
#         self.name= name #实例属性
# student1=Student("念一")
# student2=Student("张三")
# print(student1.name)
# print(student2.name)

# print(student1.school)
# print(student2.school)
# print(Student.school)

#1.4练习！！！！
# class Car:
#     wheels=4 #类属性
#     def __init__(self,brand):
#         self.brand=brand #实例属性
# car1=Car("Tesla")
# car2=Car("BMW")
# print(f"品牌为:{car1.brand},轮子数量:{car1.wheels}")
# print(f"品牌为:{car2.brand},轮子数量为:{car2.wheels}")

# #2.1类方法:类方法属于“类本身”，适合处理所有对象共享的信息，例如统计创建了多少个对象.
#         标准格式
# class 类名:
#         类属性=值
#         @classmethod
#         def 方法名(cls):
#                 return cls.类属性

# #2.2例子:
# class Student:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Student.count +=1
#     @classmethod
#     def show_count(cls):
#         print(f"当前共有{cls.count}名学生")
# Student("念一")
# Student("张三")
# Student.show_count()

# #2.3 练习:
# class Product:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Product.count +=1
#     @classmethod
#     def show_count(s):
#         print(f"当前共有{s.count}个商品")
# Product("手机")
# Product("面包")
# Product.show_count()

#3.1 静态方法：静态方法放在类中，但不需要使用对象数据self,也不需要使用类数据cls。适合放与类有关的工具功能。
#         标准格式
# class 类名:
#         @staticmethod
#         def 方法名(参数):
#                 return 结果

# #3.2例子：
# class Calculator:
#         @staticmethod
#         def add(a,d):
#                 return a+d
# result=Calculator.add(3,5)
# print(result)

# #3.3练习：
# class Converter:
#         @staticmethod
#         def converter(celsius):
#                 return celsius*9/5+32
# celsius1=Converter.converter(36)
# print(celsius1)

#4.1类型检查：isinstance()用来判断一个对象是否属于某个类，或是否属于该类的子类
#         标准格式
# isinstance(对象,类名)

#4.2例子：
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

#4.3 练习
class Person:
    pass 
class Teacher(Person):
    pass
teacher=Teacher()
isinstance(teacher,Person)
isinstance(teacher,Teacher)

# #4.4type()和isinstance()的区别:
#     a.type()检查对象是否恰好是某个类    type(对象)=类名
#     b.isinstance()检查对象是否是某个类，或该类的子类。 isinstance(对象，类名)