TempStr = input("请输入带有货币单位的值：")
if TempStr[-1] in ['$']:
    RMB = (eval(TempStr[0:-1])*6)
    print("转换后的人民币值是{:.2f}RMB".format(RMB))
elif TempStr[-1] in ['￥']:
    USD = (eval(TempStr[0:-1])/6)
    print("转换后的美元值是{:.2f}USD".format(USD))
else:
    print("输入格式错误")
