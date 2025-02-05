N = input("请输入N的值：")  # 输入一个尽可能大的值使加和结果更精确
pi = 0  # 定义pi
for k in range(int(N)):  # int将字符串转化为数字类型
    pi += 1 / pow(16, k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))  # BBP公式
print(pi)



