import json
fr = open("price2016.json","r")
ls = json.load(fr)
data = [list(ls[0].keys())]  #创建一个列表data，其第一个元素是ls中第一个字典的键（即字段名）组成的列表，并转换为列表形式，以便后续处理
for item in ls:
    data.append(list(item.values()))
fr.close()
fw = open("price2016_from_json.csv","w")
for item in data:
    fw.write(",".join(item)+"\n")
fw.close()

