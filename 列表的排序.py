ls = [2,5,7,1,6]
print("原列表：",ls)
ls.sort()
print("升序：",ls)
ls.sort(reverse=True)
print("降序：",ls)

"""
列表对象提供了sort()
方法用于对原列表中的元素进行排序。排序以后，原列表中的元素顺序将发生改变。列表对象的sort()方法的语法格式如下：

listname.sort(key=None, reverse=False)

相关的参数说明如下：

listname：表示要进行排序的列表。

key：表示指定一个从每个列表元素中提取一个比较键。（列如，设置“key = str.lower”表示在排序时不区分字母的大小写）。

reverse：可选参数，如果将其值指定为True，则表示降序排序；如果将其指定为False，则表示升序排列。默认为升序排列。

"""

