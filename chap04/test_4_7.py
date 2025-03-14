# 练习 4.7：3 的倍数 创建⼀个列表，其中包含 3〜30 内能被 3 整除的
# 数，再使⽤⼀个 for 循环将这个列表中的数打印出来。

numbers = list(range(3, 31, 3))
for number in numbers:
    print(number)