dayup,dayfactor = 1.0,0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1-dayfactor)
    else:
        dayup = dayup * (1+dayfactor)
#如果今天是周六（天数i余数为6）或周日（天数i余数为0），则 dayup 的值会减少，具体是 dayup 乘以 (1-dayfactor)
#如果今天是周一到周五中的某一天，则 dayup 的值会增加，具体是 dayup 乘以 (1+dayfactor)

print("向上五天向下两天的力量：{:.2f}.".format(dayup))


