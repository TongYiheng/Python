# random库
import random

random.seed(10)
print(random.random())                  # 生成一个[0.0, 1.0)之间的随机小数
print(random.randint(10, 20))           # randint(a,b) 生成一个[a,b]之间的整数
print(random.randrange(10, 100, 10))    # randrange(m,n[,k]) 生成一个[m,n)之间以k为步长的随机整数
print(random.getrandbits(16))           # getrandbits(k) 生成一个k比特长的随机整数
print(random.uniform(10, 100))          # uniform(a,b) 生成一个[a,b]之间的随机小数
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))               # choice(seq) 从序列seq中随机选择一个元素
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]; random.shuffle(s); print(s)    # shuffle(seq) 将序列seq中元素随机排列，返回打乱后的序列