# 练习 4.6：奇数 通过给 range() 函数指定第三个参数来创建⼀个列
# 表，其中包含 1〜20 的奇数；再使⽤⼀个 for 循环将这些数打印出
# 来。

numbers = list(range(1, 21 ,2))
for number in numbers:
    print(number)