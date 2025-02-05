excludes = {"the","and","of","you","a","i","my","in"}
def getText():
    txt = open("C:/Users/WOOKING/Desktop/hamlet.txt","r").read()  #读取文件的全部内容到变量txt中
    txt = txt.lower()  #将文本转换为小写，以便后续的单词统计不区分大小写
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch, " ")
    return txt
hamletTxt = getText()
words = hamletTxt.split()  #使用split()方法将文本分割成单词列表，存储在words变量中
counts = {}  #使用一个字典counts来统计每个单词出现的次数
for word in words:
    counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])  #遍历excludes集合中的每个停用词，并从counts字典中删除对应的项
items = list(counts.items())  #将counts字典的项（单词和它们的计数）转换成一个列表items
items.sort(key=lambda x:x[1],reverse=True)  #使用sort方法和一个lambda函数作为key参数，根据单词的计数（即列表中的第二个元素）对列表进行降序排序
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))  #遍历排序后的列表的前10个元素，并打印出每个单词及其计数