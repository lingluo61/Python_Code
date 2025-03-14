# 练习 4.9：⽴⽅推导式 使⽤列表推导式⽣成⼀个列表，其中包含前10个整数的⽴⽅。

numbers =[value ** 3 for value in range(1,11)]
for number in numbers:
    print(number)