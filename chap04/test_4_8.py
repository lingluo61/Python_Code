# 练习 4.8：⽴⽅ 将同⼀个数乘三次称为⽴⽅。例如，在 Python 中，2
# 的⽴⽅⽤ 2**3 表⽰。创建⼀个列表，其中包含前 10 个整数（1〜
# 10）的⽴⽅，再使⽤⼀个 for 循环将这些⽴⽅数打印出来。

numbers = []
for value in range(1, 11):
    numbers.append((value ** 3))
for number in numbers:
    print(number)