initial_value = 1
increased_capacity = 0.01
for i in range(365):
    if i%7 in [4,5,6,0] and i%15 != 0:   #判断其是否不等于0，如果等于0，则能力值回归1
        initial_value = initial_value*(1+increased_capacity)

print('{:.5f}'.format(initial_value))

