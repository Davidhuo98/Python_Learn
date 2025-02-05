height,weigtht = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]:"))
bmi = weigtht / pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
who,dom = "",""
if bmi < 18.5: #WHO标准
    who = "偏瘦"
elif bmi < 25:  # 18.5 <= bmi <25
    who = "正常"
elif bmi < 30:  # 25 <= bmi <30
    who = "偏胖"
else:  #bmi >= 30
    who = "肥胖"
if bmi < 18.5:#我国卫生部要求
    dom = "偏瘦"
elif bmi < 24: # 18.5 <= bmi <24
    dom = "正常"
elif bmi < 28:
    dom = "偏胖" # 24 <= bmi <28
else:  #bmi >= 28
    dom = ("肥胖")
print("BMI指标为：国际'{0}',国内'{1}'".format(who,dom))
