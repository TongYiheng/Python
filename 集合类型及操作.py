# 集合类型的定义
A = {"python", 123, ("python", 123)}
B = set("pypy123")
C = {"python", 123, "python", 123}
print(A); print(B); print(C)

# 集合操作符
# S|T 集合并
# S-T 集合减
# S&T 集合交
# S^T 集合补
# <= < >= >子集关系或者包含关系

# 集合处理方法
# S.add(x) 如果x不在集合S中，将x增加到S
# S.discard(x) 移除S中元素x，如果x不在集合S中，不报错
# S.remove(x) 移除S中元素x，如果x不在集合S中，产生KeyError异常
# S.clear() 移除S中所有元素
# S.pop() 随机返回S的一个元素，将其从S中删除并更新S，若S为空产生KeyError异常
# S.copy() 返回集合S的一个副本
# len(S) 返回结合S的元素个数
# x in S, x not in S 判断x是否在S中
# set(x) 将其他类型变量转变为集合类型
