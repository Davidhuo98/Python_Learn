import jieba
jieba.add_word("家人们")
print(jieba.lcut("真是无语了家人们"))
