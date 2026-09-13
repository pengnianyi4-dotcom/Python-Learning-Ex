# #if 条件判断
# age=18
# if age>18:
#     print("你已经成年")
# else:
#     print("你还未成年")
# #if后面有冒号，且下一行必须缩进
# score = 85
# if score >= 90:
#     print("优秀")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")
# #常用比较
# a==b#是否相等
# a!=b#是否不相等
# a>b#大于
# a>=b#大于或等于
# a<b#小于
# a<=b#小于或等于


# #for  循环遍历一组内容
# fruits = ["苹果", "香蕉", "橙子"]

# for fruit in fruits:
#     print(fruit)
#range()可以生成数字范围
# for number in range(5):
#     print(number)
#     #遵循包前不包后原则
# for number in range(1,6):
#     print(number)
#     #输出一到五
# #累加例子
# total=0
# # for number in range(1,8):
# #     total=total+number
# # print(total)
# for number in range(1,101,2):
#     total=number+total
# print(number)
# #格式 range(开始，结束，步长)

#while循环:会在条件为True时不断执行
# count=1
# while count<=5:
#     print(count)
#     count=count+1
# #循环里必须让条件最终变成 False，否则会无限循环。
# count = 1

# while count <= 3:
#     print("还在循环")
#     # count 没有变化，会永远执行
# while True:
#     command=input("输入q退出")
#     if command=="q":
#         break
# for number in range(1,6):
#     if number ==3:
#         continue
#     print(number)
# # 输出1，2，4，5 跳过了3
# count=10

# while count >=1:
#     print(count)
#     count=count-1

    



