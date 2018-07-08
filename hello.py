# coding: utf-8
i = 10
'''打印换行'''
# 打印换行
print("hello word \n  hello word")

a = "hahahah"
b = "hehehe"
print (a)

# 字符串切片
print (a[0:2])

# 字符串拼接
print (a+b)
print (a + b + str(i))

# 格式强转
c = "123"
print (int(c))

# 列表
list = [1, 2, 3]
print (len(list))
element = "插入的元素"
list.insert(1, element)   # 打印list中文乱码
print list
print element
print list.pop()
print list
list.append('追加的元素')
print list

list[1] = 3
print list