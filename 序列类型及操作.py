# 元组类型及操作
creature = "cat", "dog", "tiger", "human"
color = (0x001100, "blue", creature)
print(creature)
print(color[-1][2])

# 列表类型及操作
ls = ["cat", "dog", "tiger", 1024]
lt = ls                 # 赋值，仅传递引用，lt和ls均指向同一个列表
                        # ls[i]=x 替换列表ls第i元素为x
ls[1:2]=[1, 2, 3, 4]    # ls[i:j:k]=lt 用列表lt替换ls切片后所对应元素子列表
print(ls)
                        # del ls[i] 删除列表第i元素
del ls[::3]             # del ls[i:j:k] 删除列表ls中第i到第j以k为步长的元素
print(ls)
                        # ls+=lt 更新列表ls，将列表lt元素增加到列表ls中
ls *= 2                 # ls*=n 更新列表ls，其元素重复n次
print(ls)

ls2 = ["cat", "dog", "tiger", 1024]
ls2.append(1324)        # ls.append(x) 在列表ls最后增加一个元素x
                        # ls.clear() 删除列表ls中所有元素
                        # ls.copy() 生成一个新列表，赋值ls中所有元素
ls2.insert(3, "human")  # ls.insert(i,x) 在列表ls的第i位置增加元素x
                        # ls.pop(i) 将列表ls中第i位置元素取出并删除该元素
                        # ls.remove(x) 将列表ls中出现的第一个元素x删除
ls2.reverse()           # ls.reverse() 将列表ls中的元素反转
