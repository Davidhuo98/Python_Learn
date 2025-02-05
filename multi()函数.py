def multi(*args):
    # 如果没有提供参数，则返回1（乘法的单位元素）
    if not args:
        return 1

        # 使用reduce函数从functools模块来计算乘积
    # 注意：在Python 3中，reduce函数已经从全局命名空间中移除，并移到了functools模块
    from functools import reduce
    return reduce(lambda x, y: x * y, args)


# 测试函数
print(multi(1, 2, 3, 4))  # 输出: 24
print(multi(10))  # 输出: 10
print(multi())  # 输出: 1