#1.列表 按照顺序保存多个值
# fruits =["Apple","Banana","Orange"]
# print(fruits)
# print(fruits[0]) #0为第一个元素,输出Apple
# print(fruits[-1])#-1为最后一个元素 输出Orange

# #添加元素
# fruits.append("watermelon") #默认添加到末尾
# fruits.remove("Apple") #指定删除
# print(fruits) 

# #修改元素
# fruits[0] = "Pear"
# print(fruits)

#配合循环使用
# for i in fruits:
#     print(f"我喜欢吃{i}")

#小练习：创建一个包含 3 个数字的列表，输出其中最大的数字。
# numbers = [5,10,45]
# # print(max(numbers)) #35

# largest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest=i
# print(i)



#2.字典
# student={
#     "name":"小明",
#     "age":18,
#     "score":92
# }
# print(student["name"]) #小明
# print(student["score"]) #92
# # 修改或新增内容
# student["score"]= 95
# student["city"]= "上海"  #新增  默认添加到末尾
# print(student)
# #若内容不存在字典当中
# print(student.get("phone"))  #输出None
# print(student.get("phone","未找到该数据"))

#2.1遍历字典
# for key,value in student.items():
#     print(f"{key}:{value}")
# book={
#     "Title":"凡人修仙传",
#     "Author":"忘语",
#     "price":80
# }
# # print(f"<{book["Title"]}>作者是{book["Author"]},价格是{book['price']}元")

#3.1集合:适合存放“不重复”的数据. 
# numbers={1,1,1,2,2,2,3,3,3}
# print(numbers) #输出{1, 2, 3}
#重复值会自动被去掉。集合没有固定顺序，所以不能用 numbers[0] 按位置取值

#3.2常见操作
# colors={"红","绿","蓝"}
# colors.add("黄")#添加
# colors.remove("绿") #删除
# print(colors)

# #3.3检查某个值是否存在:
# if "红" in colors:
#     print("有红色")
# #3.4 实际例子 给列表去重
# names = ["小明","小刚","小明","小刚"]
# unique_names = set(names) #列表转换为了集合
# print(unique_names)
# unique_list=list(unique_names) #集合变回列表
# print(unique_list)


#4.1 元组:与列表很像,但创建后不能修改,适合保存固定不变的数据
# point=(10,20)
# print(point[0])
# print(point[1])
#元组可以拆分到多个变量:
# name,age =("念一",19)
# print(name)
# print(age)
#不能修改,修改会报错
# name[0]="Peng"
#4.2 常见用途
# def get_user():
#     return "小明",19
# name,age=get_user()
# print(f"{name},{age}岁")

# #区别简单记：
# - 列表 []：可修改。
# - 元组 ()：不可修改。
# - 集合 {}：不重复、无固定顺序。
# - 字典 {key: value}：按键保存值