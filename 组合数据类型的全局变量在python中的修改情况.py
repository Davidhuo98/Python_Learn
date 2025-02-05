ls = []  #全局变量为空值，但经由函数运行发生了变化
def func(a,b):
    ls.append(b)
    return a*b
s= func("knock~",2)
print(s,ls)
