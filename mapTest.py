# coding: utf-8
# 字典：类似于json
dic = {"name" : "xqe","age" : 26, "sex:":"男"}
print dic
print dic.keys()
print dic.values()
print dic.get("name")
dic["name"] = "xieqien"
print dic

# 遍历字典
# 第一种
for i in dic:
    print (i,dic[i])

# 第二种 该方法多了一个将字典转换为列表的操作，在数据量特别大的时候影响性能
for key,value in dic.items():
    print (key,value)