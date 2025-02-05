import random
k = random.randint(0,100)
n = int(input("请输入你猜测的数字:"))
count = 0
if n > 100:
    print("你输入的数字不正确，超过100")

while n != k:
    if 100 > n > k:
        print("遗憾，太大了")
    elif n < k:
        print("遗憾，太小了")
    count += 1
    n = int(input("请再试一次："))  # 提示用户再次输入

print("预测{}次，猜对了".format(count + 1))  # 加上初始的猜测次数
