import math
a = eval(input("请输入整数a:"))
b = eval(input("请输入整数b:"))
m = math.gcd(a,b)
n = int((a*b)/m)
print("a,b的最大公约数是:{},最小公倍数是:{}".format(m,n))







