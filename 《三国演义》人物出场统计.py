import jieba
excludes = {"意谓","将军","却说","二人","不可","不能","如此","荆州","天下","如此","这里","商议","如何","主公"}
txt = open("C:/Users/WOOKING/Desktop/三国演义.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word)==1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word =="云长":
        rword = "关羽"
    elif word == "玄德" or word =="玄德曰":
        rword = "刘备"
    elif word == "孟德" or word =="丞相":
        rword = "曹操"
    else:
        rword = word
        counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())  #将counts字典的项（单词和它们的计数）转换成一个列表items
items.sort(key=lambda x:x[1],reverse=True)
for i in range(5):
    word,count = items[i]
    print("{0:<5}{1:5}".format(word,count))
