number = input('请输入一个数字：')
number_int = int(number)
if number_int/10000 >= 1:
    if number[0]==number[4] and number[1]==number[3]:
        print(number)
    else:
        print('这个数不是回文数')
else:
    print('输入的数字不是5位数')