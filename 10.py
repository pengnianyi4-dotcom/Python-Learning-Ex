#1.1类型提示：类型提示用于说明变量，函数参数和返回值预期是什么类型。让代码更清楚，也方便编辑器发现潜在错误
            #主要给开发者和工具看的
#     格式：
# 变量名：类型=值
# def 函数名(参数:类型)
#     return 结果

# name:str="小明"
# age:int=19

# def add(a:int,b:int)->int:
#     return a+b


# result:int = add(3,5)
# print(result)



# def introduce(name:str,age:int)->str:
#     return f"我叫{name},今年{age}岁。"
# print(introduce("小明",19))

#2.1容器类型提示：除了 str、int，列表、字典等也可以写类型提示，说明其中存放什么数据。
#         标准格式：
# list[元素类型]
# dict[键类型，值类型]
# tuple[元素类型,元素类型]
# set[元素类型]
# names: list[str] = ["小明", "小红"]
# scores: dict[str, int] = {
#     "小明": 90,
#     "小红": 95
# }
# point: tuple[int, int] = (10, 20)
# numbers: set[int] = {1, 2, 3}

# print(names)
# print(scores)
# print(point)
# print(numbers)

#3.1可选类型:有些变量或函数结果可能是某种类型，也可能没有值。可以用类型None表示这种情况。
#         标准格式：
# 变量名：类型| None = None
# def 函数名() ->类型 | None:
#         return 值或None

# #3.2例子：
# def find_score(name:str) -> int |None:  #表示函数可能返回整数，也有可能返回None.
#     scores={
#         "小明":90,
#         "小红":95
#     }
#     return scores.get(name)
# score = find_score("小刚")
# if score is None:
#     print("没有找到成绩")
# else:
#     print(f"成绩:{score}")


# #3.3练习：
# def find_age(name:str) -> int |None:
#     ages={
#         "小明":19,
#         "小红":17
#     }
#     return ages.get(name)
# age=find_score("小刚")
# if age is None:
#     print("No")
# else:
#     print(f"成绩:{age}")


# # #4.1默认参数和类型提示：默认参数让调用函数时可以不传入某个参数;PYTHON会使用预先设定的默认值
# #         标准格式：
# # def 函数名(参数：类型 = 默认值) -> 返回类型：
# #     return 结果

# # #4.2例子：
# # def greet(name:str,greeting:str = "你好") ->str:
# #     return f"{greeting},{name}!"
# # print(greet("小明"))
# # print(greet("小红","早上好"))

# # #4.3 练习:
# # def introduce(name:str,city:str = "上海") -> str:
# #     return f"我叫{name},来自{city}。"
# # print(introduce("念一"))
# # print(introduce("小红","北京"))

# #5.1关键字参数：关键字参数让你通过“参数名=值”的形式传入数据，代码更清楚，也可以改变传参顺序。
# #     标准格式：
# # 函数名(参数名1=值1，参数名2=值2)

# #5.2例子:
# def create_user(name: str, age: int, city: str) -> str:
#     return f"{name},{age}岁，来自{city}"


# print(create_user(name="小明", age=18, city="上海"))
# print(create_user(city="北京", name="小红", age=20))

# #6.1可变数量的位置参数*args  让函数接受任意数量的位置参数。函数内部会把它们收集成一个元组。
# #         标准格式：
# # def 函数名(*args: 类型) -> 返回类型:
# #      #args是元组
# #      pass

# def calculate_total(*prices:float) -> float:
#     return sum(prices)

# print(calculate_total(19.0,25.5,10.0))

# def find_max(*number:int) -> int:
#     return max(number)
# print(find_max(3,8,2,9,117))

# # #7.2**kwargs可变数量的关键字参数：让函数接受任意数量的“参数名=值”。函数内部会把它们收集成一个字典。
# #         标准格式：
# # def 函数名(**kwarges:类型)->返回类型:
# #     # kwrges是字典
# #     pass
# def show_user(**info:str) ->None:
#     for key,value in info.items():
#         print(f"{key}:{value}")
# show_user(name="小明",city="上海",job="学生")

# #7.3练习：
# def show_product(**product:str) ->None:
#     for key,value in product.items():
#         print(f"{key}:{value}")
# show_product(name="手机",price="999999",color="黑色")



# #同时使用普通参数，*args,**kwargs
# #         格式：
# # def 函数名(普通参数，*args,**kwargs):
# #         pass
#                 #参数顺序必须是普通参数，args,kwargs
# def show_order(customer: str, *foods: str, **options: str) -> None:
#     print(f"顾客：{customer}")
#     print(f"食物：{foods}")
#     print(f"选项：{options}")


# show_order(
#     "小明",
#     "汉堡",
#     "薯条",
#     "可乐",
#     spicy="微辣",
#     takeaway="是"

# #练习：
# def create_profile(name:str,*hobbies:str,**details:str)->None:
#     print(f"顾客：{name}")
#     print(f"爱好：{hobbies}")
#     for key,value in details.items():
#         print(f"{key}:{value}")
# create_profile(
#     "小红",
#     "阅读",
#     "跑步",
#     city="北京",
#     job="设计师"
# )

# #8.1参数解包：*和**不只可以用于定义函数参数，也可以在调用函数时把列表，元组或”字典拆开传入函数。
#   格式：
# 函数名(*列表或元组)

# 函数名(**字典)


# def show_book(title:str,author:str,price:float)->None:
#     print(f"{title}作者：{author},价格:{price}")
# book = {
#     "title": "Python 入门",
#     "author": "张三",
#     "price": 59.9
# }
# show_book(**book)



#9.1列表推导式：用一行代码创建列表，尤其适合“遍历，处理，筛选”数据。
#     格式：
# [处理后的值 for 元素 in 可迭代对象]
#     带条件的
# [处理后的值 for 元素 in 可迭代对象 if 条件]

# numbers = [1, 2, 3, 4, 5]

# squares = [number ** 2 for number in numbers]

# print(squares)

# even_squares = [
#     number ** 2
#     for number in numbers
#     if number % 2 == 0
# ]

# print(even_squares)

#9.2练习：
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers=[number 
             for number in numbers 
             if number %2!=0
             ]
print(odd_numbers)