import math
dayup,dayfactor = 1.0,0.010
for i in range(360):
    if i % 30 <= 10:
        dayup = dayup * (1 + dayfactor)
    else:
        dayup = dayup * (1 + 0)


print("向上十天，不变二十天的力量：{:.2f}.".format(dayup))
