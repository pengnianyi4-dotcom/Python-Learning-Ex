name="Xiao Ian"   #变量：用名字保存数据
age=19
height=1.84
is_student=True

#输出内容
print(name)
print(age)
print(height)
pirnt("姓名：",name)

#Python 常见数据类型
text="念一" #str
count=100 #int
price=1.99#float
valid=False #bool
nothing=None #None

 #查看一个值的类型:print(type(.....))
print(type(text))
print(type(count))

#基础运算
a=12
b=12
print(a+b)#加法
print(a-b)#减法
print(a*b)#乘法
print(a/b)#除
print(a//b)#取整数
print(a%b)#取余
print(a**b)#幂

#字符串可以拼接，数值需要转换
name="Ian"
age=19
print(name+"今年"+str(age)+"岁")
print(f"{name}今年{age}岁")
# 前面的 f 表示：字符串中 {} 里的内容要当作 Python 表达式计算。
a=10
b=10
print(f"{a}+{b}={a+b}")
#输出 10+10=20
