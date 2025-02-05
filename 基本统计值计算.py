from math import sqrt
def getNum():    #获取用户输入
    global nums
    nums = []
    iNumStr = input("请输入数字（直接输入回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（直接输入回车退出）：")
    return nums
def mean(numbers):  #计算平均值
    s = 0.0
    for num in numbers:
        s = s+num
        return s/len(numbers)
def dev(numbers,mean):  #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev+(num-mean)**2
    return sqrt(sdev/len(numbers)-1)
def median(numbers):  #计算中位数
    new = sorted(numbers,reverse=True)
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size//2-1] + new[size//2])/2
    else:
        med = new[size//2]
    return med
def compare():
    new = sorted(nums)
    print("最大值为：",[-1])
    print("最小值为：",[0])

n = getNum()  #主体函数
m = mean(n)
print("平均值：{},标准差：{:.2},中位数：{}.".format(m,dev(n,m),median(n)))