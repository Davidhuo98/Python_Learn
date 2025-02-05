def isNum(num):
    if type(num) is int or type(num) is float or type(num) is complex:
        return True
    else:
        return False
str = eval(input("请输入一个字符串："))
print(isNum(str))
