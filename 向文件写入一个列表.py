fname = input("请输入要写入的文件：")
fo = open(fname, "r")
ls = ["唐诗\n", "宋词\n", "元曲\n"]  # 添加换行符以便更好地分隔内容
fo.writelines(ls)
fo.seek(0)  # 将文件位置指针移动到文件开头
for line in fo:
    print(line, end='')  # 去掉print的默认换行符，因为文件中已经包含了换行符
fo.close()