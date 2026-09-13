#异常处理 这让程序遇到错误时不至于直接中断
try:
    number=int(input("请输入一个数字"))
    print(10/number)
except ValueError:
    print("输入的不是数字")
except ZeroDivisionError:
    print("不能除以0")
#try放可能出错的代码，except处理对应的错误。
#无论是否出错都要执行的代码，放在finally


