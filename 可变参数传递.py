def fact(n, *b):            # b为可变参数
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s


print(fact(10, 3))
print(fact(10, 3, 5, 8))
