import random

# 假设我们有一个秘密数字在1到100之间
secret_number = random.randint(1, 100)

while True:
    try:
        # 尝试将输入转换为整数
        guess = int(input("请猜一个1到100之间的整数："))

        # 检查猜测是否在范围内
        if guess < 1 or guess > 100:
            print("猜测的数字必须在1到100之间！")
            continue  # 跳回到循环的开始

        # 检查猜测是否正确
        if guess == secret_number:
            print("恭喜你，猜对了！")
            break  # 退出循环
        elif guess < secret_number:
            print("你猜的数字太小了。")
        else:
            print("你猜的数字太大了。")

    except ValueError:
        # 如果输入的不是整数，捕获ValueError异常并给出提示
        print("输入内容必须为整数！")
