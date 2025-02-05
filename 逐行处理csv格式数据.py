fo = open("price2016.csv", "r")
ls = []
for line in fo:  #遍历文件 fo 中的每一行
    line = line.replace("\n","") #去除每行末尾的换行符（\n），因为在读取文件时，每行的末尾通常会包含一个换行符。
    ls = line.split(",")  # 将去除换行符后的行（line）按照逗号（,）分割成多个字符串，并将这些字符串存储在 ls 中
    lns = ""  #在循环的每次迭代中，都初始化一个空字符串 lns
    for s in ls:  # 遍历 ls中的每个元素 s
          lns += "{}\t".format(s)  #将每个元素 s 转换为字符串（虽然 s 已经是字符串），并在其后添加一个制表符（\t），然后将结果追加到 lns 中
    print(lns)
fo.close()