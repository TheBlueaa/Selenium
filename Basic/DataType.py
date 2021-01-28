'''
# list
# 定义
listsone = [1,2,3,'a',5]
# 打印
print(listsone)
print("——————————————我是分割线————————————————-")
# 打印第四个
print(listsone[3])
print("——————————————我是分割线————————————————-")
# 打印倒数第一个
print(listsone[-1])
print("——————————————我是分割线————————————————-")
# 修改第三个元素为'b'
listsone[2] = 'b'
print(listsone)
print("——————————————我是分割线————————————————-")
# 在末尾添加元素
listsone.append('x')
print(listsone)
print("——————————————我是分割线————————————————-")
# 删除列表中的第二个元素
listsone.pop(1)
print(listsone)
print("——————————————我是分割线————————————————-")
'''


'''
# tuple 元祖————这个错误出现是因为执行元组之间的合并
tupone = ("a","c",7,11)
tuptwo = (1,3,5,7,9,"af")
tuptre = ("erro")
print(tuptwo)
print("——————————————我是分割线————————————————-")
# 链接/拼接元祖
tupthr = tupone + tuptwo
tupfiv = tuptre + tupone
# 正确
print(tupthr)
# 错误————这个错误出现是因为执行元组之间的合并，需要在tuptre的字符串后面添加逗号"  ，"
print(tupfiv)
print("——————————————我是分割线————————————————-")
# 复制元祖
tupfour = ("人类的本质_")
print(tupfour * 3)
print("——————————————我是分割线————————————————-")
# 数组可变，可添加，删除，元祖不可变
'''




'''
# 字典
dicts = {
    "username" : "zhangsan",
    "password" : "123456",
    }
# 打印字典中所有的key
print(dicts.keys())
print("——————————————我是分割线————————————————-")
# 打印字典中所有的value
print(dicts.values())
print("——————————————我是分割线————————————————-")
# 向字典中添加键值对
dicts["sex"] = "人妖"
dicts["age"] = 23
print(dicts)
# 循环打印字典中的key和value————————items()是指将字典中的所有元素以列表方式返回，如果想要单独循环一个字典的key或者value，则需要用字典.keys/values去遍历
for k, v in dicts.items():
    print("dicts keys is %r And value is %r" % (k, v))
print("——————————————我是分割线————————————————-")
for k in dicts.keys():
    print("dicts key is %r " %k )
print("——————————————我是分割线————————————————-")
for v in dicts.values():
    print("dicts value is %r " %v )
print("——————————————我是分割线————————————————-")
#删除键是"age"的项
dicts.pop("age")
# 打印字典以列表方式返回
print(dicts.items())
'''
