# 字符串操作符
print("123"+"456")                          # 连接两个字符串
print(5 * "123")                            # 复制n次字符串x
print("123" in "123456")                    # 如果x是s的子串，返回True，否则返回False

# 字符串处理函数
print(len("一二三456"))                     # 返回字符串的长度，注意中文字符
print(str(1.23))                            # 返回任意类型对应的字符串形式
print(hex(425)+" "+oct(425))                # 返回整数x的十六进制(hex)或八进制(oct)小写形式字符串
print(chr(10004)+" "+chr(9801))             # chr(u) 返回Unicode编码对应的字符
print(ord(chr(9801)))                       # ord(x) 返回字符对应的Unicode编码

# 字符串处理方法
print("AbCd".lower()+" "+"AbCd".upper())    # 返回字符串的副本，全部字符大写(upper)或小写(lower)
print("A,B,C".split(","))                   # str.split(sep=None) 返回一个列表，由str根据sep被分隔的部分组成
print("an apple a day".count("a"))          # str.count(sub) 返回子串sub在str中出现的次数
print("python".replace("n", "n123.io"))     # str.replace(old,new) 返回字符串str副本，所有old子串被替换为new
print("python".center(20, "="))             # str.center(width [,fillchar])字符串str根据宽度width居中，fillchar可选
print("= python= ".strip(" =np"))           # str.strip(chars) 从str中去掉在其左侧和右侧chars中列出的字符
print(",".join("12345"))                    # str.join(iter) 在iter变量除最后元素外每个元素后增加一个str，主要用于字符串分隔

# 字符串类型的格式化
print("{0:=^20}".format("PYTHON"))          # <填充的单个字符，默认为空格> <对齐>(<左对齐，>右对齐，^居中对齐) <宽度>
print("{0:,.2f}".format(12345.6789))        # <,>数字的千位分隔符 <.精度>浮点数小数精度或字符串最大输出长度 <类型>整数类型b,c,d,o,x,X 浮点数类型e,E,f,%
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))
