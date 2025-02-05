initial_value = 1
for i in range(365):
    if i%7 in [4,5,6,0]:
        initial_value = initial_value*(1+0.01)

print('{:.5f}'.format(initial_value))