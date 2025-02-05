def isPrime(n):
    # 首先检查n是否小于2，因为小于2的数不是质数
    if n < 2:
        return False

        # 检查n是否是一个整数
    if not isinstance(n, int):
        raise ValueError("输入必须是一个整数")

        # 检查n是否可以被2到sqrt(n)之间的任何数整除
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

            # 如果以上条件都不满足，则n是质数
    return True
str = eval(input("请输入一个字符串："))
print(isPrime(str))

# 测试函数
"""
try:
    print(isPrime(17))  # 应该返回True
    print(isPrime(4))  # 应该返回False
    print(isPrime(3.14))  # 应该抛出异常
except ValueError as e:
    print(e)
"""
