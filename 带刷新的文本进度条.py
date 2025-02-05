import time
scale = 50
print("执行开始".center(scale//2,'-'))
t = time.perf_counter() #Python3.x 不再支持time.clock()，但在调用时依然包含该方法,应换成time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100 #进度百分比
    t -= time.perf_counter() #同程序第四行
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),end='')
    time.sleep(0.05) #time.sleep()来自 time 模块，用于使程序暂停执行指定的秒数
print("\n"+"执行结束".center(scale//2,'-'))