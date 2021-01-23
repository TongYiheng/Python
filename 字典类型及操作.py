# 字典类型定义
d = {"中国": "北京", "美国": "华盛顿", "法国": "巴黎"}
print(d["中国"])
de = {}  # 定义空字典
print(type(de))
de["a"] = 1
de["b"] = 2

# 字典处理函数及方法
# del d[k] 删除字典d中键k对应的数据值
# k in d 判断键k是否在字典d中
print(d.keys())  # d.keys() 返回字典d中所有的键信息
print(d.values())  # d.values() 返回字典d中所有的值信息
# d.items() 返回字典d中所有的键值对信息
d.get("巴基斯坦", "伊斯兰堡")  # d.get(k,<default>) 键k存在，则返回相应值，不存在则返回<default>值
# d.pop(k,<default>) 键k存在，则取出相应值，不存在则返回<default>值
d.popitem()  # d.popitem() 随机从字典d中取出一个键值对，以元组形式返回
# d.clear() 删除所有的键值对
# len(d) 返回字典d中元素的个数