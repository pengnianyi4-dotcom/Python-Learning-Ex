# #1.1with语句：with常用于操作文件。会在代码执行结束后自动关闭文件，即使中途发生错误也更安全
#     标准格式：
# with open("文件名","模式",encoding="utf-8") as 文件变量：
#     #操作文件
    #常见模式
#"r"读取文件
#"w"写入文件
# "a"追加内容到文件末尾

# #1.2例子：
# with open("note.txt","w",encoding="utf-8") as file:
#     file.write("学习python\n")
#     file.write("继续练习\n")
# with open("note.txt","r",encoding="utf-8") as file:
#     content=file.read()
# print(content)

# #1.3练习:
# with open("message.txt","w",encoding="utf-8") as file:
#     file.write("你好\n")
#     file.write("Pyhton\n")
# with open ("message.txt","r",encoding="utf-8") as file:
#     content=file.read()
# print(content)

#1.4"a"追加文件内容：保留原文件内容，并把新内容写到最后
#         格式：
# with open("文件名","a",encoding="utf-8") as file:
#      file.write("要追加的内容\n")

#1.5练习：
# with open("todo.txt","w",encoding="utf-8") as file:
#     file.write("学习PYTHON\n")
# with open("todo.txt","a",encoding="utf-8") as file:
#     file.write("完成练习\n")
# with open("todo.txt","r",encoding="utf-8") as file:
#     content=file.read()
# print(content)


# #2.1逐行读取文件:文件很大时，不建议一次用read()读取全部内容。可以逐行读取，更节省内存。
#     格式
# with open("文件名","r",encoding="utf-8") as file:
#     for line in file:
#         print(line)


#练习：
with open("todo.txt","r",encoding="utf-8") as file:
    for line in file:
        print(line.strip())   
        #每行通常自带结尾换行符 \n；strip() 会去掉开头和结尾的空白字符，包括这个换行符，避免打印时出现空行。

with open("scores.txt","w",encoding="utf-8") as file:
    file.write("小明,90\n")
    file.write("小红,95\n")
    file.write("小刚,88\n")
with open("scores.txt","r",encoding="utf-8") as file:
    for line in file:
        print(line.strip())

#2.2:pathlib:路径与文件判断  用更清晰的方式处理文件路径，判断文件是否存在，读取或写入文本
#     格式：
# from pathlib import Path
# path = Path("文件名")
# path.exists()
# path.read_text(encoding="utf-8")
# path.write_text("内容",encoding="utf-8")

#3.1  JSON:这是常用的数据保存与传输格式，外形很像Python字典
#         格式：
# import json
# json.dump(字典，文件对象，ensure_ascii=False,indent=2)
# 数据=json.load(文件对象)  
#  
# import json

student = {
    "name": "小明",
    "age": 18,
    "scores": [90, 95, 88]
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False, indent=2)


with open("student.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data["name"])
print(data["scores"])    